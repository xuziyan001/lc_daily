
"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 
[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start = 0
        end = 0
        current_sum = 0
        n = len(nums)
        m = n+1
        while end <= n:
            if current_sum < target:
                if end == n:
                    break
                current_sum += nums[end]
                end += 1
            else:
                if end - start < m:
                    m = end - start
                current_sum -= nums[start]
                start += 1
        if current_sum > target and end-start < m:
            m = end-start
        return m if m != n+1 else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(4, [1,4,4]))
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))



