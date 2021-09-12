"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def __dfs(i, j):
            if grid[i][j] == '0':
                return
            grid[i][j] = 'M'
            if i-1 >= 0 and grid[i-1][j] == '1':
                __dfs(i-1, j)
            if i+1 < m and grid[i+1][j] == '1':
                __dfs(i+1, j)
            if j-1 >= 0 and grid[i][j-1] == '1':
                __dfs(i, j-1)
            if j+1 < n and grid[i][j+1] == '1':
                __dfs(i, j+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    __dfs(i, j)
                    count += 1
        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))