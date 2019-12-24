from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] > target:
                return i
            elif nums[i] < target:
                continue
            else:
                return i
        return len(nums)
