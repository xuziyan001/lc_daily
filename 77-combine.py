"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

"""

"""
思路与全排列一致，筛选出符合条件的加入output
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        output = []
        backtrack()
        return output


if __name__ == '__main__':
    print(Solution().combine(4, 4))
    print(Solution().combine(8, 4))
    print(Solution().combine(12, 4))
