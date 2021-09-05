"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。
"""
from tool import print_matrix


class Solution:
    def minCut(self, s: str) -> int:
        if len(set(list(s))) == 1:
            return 0
        length = len(s)
        dp = [[True] * length for _ in range(length)]
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        if dp[0][length-1]:
            return 0
        dp2 = [10000] * length
        for i in range(length):
            if dp[0][i]:
                dp2[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        dp2[i] = min(dp2[i], dp2[j]+1)
        return dp2[-1]


if __name__ == '__main__':
    s = "cbbbcc"
    print(Solution().minCut(s))