from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        origin = nums.copy()
        nums.sort()
        for index in range(len(nums)):
            new_target = target - nums[index]
            if new_target == nums[index] and nums.count(new_target) > 1:
                first = origin.index(new_target)
                second = origin.index(new_target, first+1, len(nums)+1)
                return [first, second]
            else:
                try:
                    nums.index(new_target)
                except:
                    continue
                else:
                    return [origin.index(nums[index]), origin.index(new_target)]


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9)) #== [0,1]
    print(Solution().twoSum([11,7,11,16], 22)) #== [0,2]
    print(Solution().twoSum([3,3], 6)) #== [0,2]
