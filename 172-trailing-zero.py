"""
给定一个整数 n ，返回 n! 结果中尾随零的数量。
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 0
        while n:
            n, _ = divmod(n, 5)
            total += n
        return total


if __name__ == '__main__':
    print(Solution().trailingZeroes(25))
