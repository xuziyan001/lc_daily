"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，
其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

if __name__ == '__main__':
    print(Solution().singleNumber([2,2,2,1]))
