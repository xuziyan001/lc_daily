from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        dp = [[1] * n for i in range(m)]
        first_row = False
        first_col = False
        for i in range(m):
            if first_col:
                dp[i][0] = 0
            else:
                if obstacleGrid[i][0] == 1:
                    dp[i][0] = 0
                    first_col = True
        for i in range(n):
            if first_row:
                dp[0][i] = 0
            else:
                if obstacleGrid[0][i] == 1:
                    dp[0][i] = 0
                    first_row = True
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    l = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
    print(Solution().uniquePathsWithObstacles(l))
    l = [[1]]
    print(Solution().uniquePathsWithObstacles(l))
    l = [[1,0]]
    print(Solution().uniquePathsWithObstacles(l))
