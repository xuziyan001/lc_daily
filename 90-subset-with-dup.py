"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
"""
"""
backtrace可以理解为要与不要第i个元素的所有子集
"""


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrace(index=0, current=[]):
            if tuple(current) not in s:
                res.append(current[:])
                s.add(tuple(current))
            for i in range(index, n):
                current.append(nums[i])
                backtrace(i+1, current)
                current.pop()
        res = []
        s = set()
        nums.sort()  # 必须要排序
        n = len(nums)
        backtrace()
        return res


if __name__ == '__main__':
    l = [1,2,2,2]
    print(Solution().subsetsWithDup(l))
    l = [1,2]
    print(Solution().subsetsWithDup(l))
