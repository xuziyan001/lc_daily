from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i, j = 0, 0
        current = nums[0]
        count = 0
        while j < len(nums):
            if nums[j] == current:
                if count == 2:
                    j += 1
                else:
                    nums[i] = nums[j]
                    i += 1
                    j += 1
                    count += 1
            else:
                nums[i] = nums[j]
                current = nums[i]
                i += 1
                j += 1
                count = 1
        return i


if __name__ == '__main__':
    l = [0,0,1,1,1,1,2,3,3]
    print(Solution().removeDuplicates(l))
    print(l)