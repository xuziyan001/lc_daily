from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        num = nums[0]
        if num >= len(nums)-1:
            return 1
        range_min = 1
        range_max = num
        count = 0
        while range_max < len(nums)-1:
            t_min, t_max = range_min, range_max
            for i in range(range_min, range_max+1):
                m = i + nums[i]
                if m > t_max:
                    t_max = m
                    t_min = i
            range_min, range_max = t_min, t_max
            count += 1
        return count+1
