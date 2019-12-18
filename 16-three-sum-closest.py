from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == target:
                        return s
                    if abs(s - target) < abs(closest - target):
                        closest = s
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
        return closest


if __name__ == '__main__':
    print(Solution().threeSumClosest([-1,2,1,-4], 1))
    print(Solution().threeSumClosest([0,2,1,-3], 1))
