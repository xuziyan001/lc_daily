class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]
        dp[0] = list(range(n+1))
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[m][n]


if __name__ == '__main__':
    print(Solution().minDistance("a", "asd"))
    word1 = "horse"; word2 = "ros"
    print(Solution().minDistance(word1, word2))
    word1 = "intention"; word2 = "execution"
    print(Solution().minDistance(word1, word2))
