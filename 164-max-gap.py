"""

给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。
"""
from typing import List

# 桶排序
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        buf = [0] * n
        max_val = max(nums)
        exp = 1
        while exp <= max_val:
            cnt = [0] * 10
            for each in nums:
                digit = each//exp % 10
                cnt[digit] += 1
            for i in range(1,10):
                cnt[i] += cnt[i-1]
            for i in range(n-1, -1, -1):
                digit = nums[i] // exp % 10
                buf[cnt[digit]-1] = nums[i]
                cnt[digit] -= 1
            exp *= 10
            nums = buf[:]
        m = 0
        for i in range(1,n):
            m = max(m, nums[i]-nums[i-1])
        return m


if __name__ == '__main__':
    l = [3,6,9,1]
    print(Solution().maximumGap(l))
    l = [15252,16764,27963,7817,3,44,569]
    print(Solution().maximumGap(l))
