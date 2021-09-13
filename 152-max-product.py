"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），
并返回该子数组所对应的乘积
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_min = nums[0]
        f_max = nums[0]
        tmp = nums[0]
        for each in nums[1:]:
            t1 = f_min
            t2 = f_max
            f_min = min(t1*each, t2*each, each)
            f_max = max(t1*each, t2*each, each)
            tmp = max(f_max, tmp)
        return tmp


if __name__ == '__main__':
    l = [-2,0,-1]
    print(Solution().maxProduct(l))
    l = [3,4,-1,33,-1]
    print(Solution().maxProduct(l))
    l = [2,3,-2,4]
    print(Solution().maxProduct(l))
