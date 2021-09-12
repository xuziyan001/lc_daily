"""
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。

进阶：

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为O(1) 的原地算法解决这个问题吗？
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k <= 0:
            return
        def __rotate(i, j):
            while j > i:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j -= 1
        print(nums)
        __rotate(0,n-k-1)
        __rotate(n-k,n-1)
        __rotate(0, n-1)
        print(nums)


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7]
    Solution().rotate(l,3)