"""

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        s = set(nums)
        for each in s:
            if each-1 in s:
                continue
            count = 1
            start = each
            while start+1 in s:
                count += 1
                start += 1
            if count > max_len:
                max_len = count
        return max_len


if __name__ == '__main__':
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
