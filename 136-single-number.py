"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for each in nums:
            n ^= each
        return n


if __name__ == '__main__':
    print(Solution().singleNumber([2,2,1]))

