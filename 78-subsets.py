"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

"""

"""
TODO 这种backtrace的思维有待加强
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrace(index=0, current=[]):
            res.append(current[:])
            for i in range(index, n):
                current.append(nums[i])
                backtrace(i+1, current)
                current.pop()
        nums = list(set(nums))
        n = len(nums)
        res = []
        backtrace()
        return res


if __name__ == '__main__':
    l = [1,2,3,4]
    print(Solution().subsets(l))
