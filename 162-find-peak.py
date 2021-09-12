"""
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设nums[-1] = nums[n] = -∞ 。

"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        def __dfs(start, end):
            if end >= start:
                mid = start + (end-start)//2
                if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                    return mid
                t = __dfs(start, mid-1)
                if t:
                    return t
                t = __dfs(mid+1, end)
                return t
        return __dfs(1, n-2)


if __name__ == '__main__':
    l = [1,2,3,4,1]
    print(Solution().findPeakElement(l))
    l = [1,2,1,3,5,6,4]
    print(Solution().findPeakElement(l))