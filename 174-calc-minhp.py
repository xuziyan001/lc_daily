"""
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由
M x N 个房间组成的二维网格。
我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（
若房间里的值为负整数，则表示骑士将损失健康点数）；
其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球
（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

"""
import sys
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if len(dungeon) == 0 or len(dungeon[0]) == 0:
            return -1
        m = len(dungeon)
        n = len(dungeon[0])
        starter = (1, 1)
        # res = []
        self.min_starter = sys.maxsize

        def __route(i, j, min_cost):
            start = min_cost[0]
            remain = min_cost[1]
            r = remain + dungeon[i][j]
            if r > 0:
                remain = r
            else:
                remain = 1
                start = start - r + 1
            if i != m - 1:
                __route(i + 1, j, (start, remain))
            if j != n - 1:
                __route(i, j + 1, (start, remain))
            if i == m - 1 and j == n - 1:
                # res.append((start, remain))
                if start < self.min_starter:
                    self.min_starter = start

        __route(0, 0, starter)
        # print(res)
        return self.min_starter

    def calculateMinimumHP2(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10 ** 9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]


if __name__ == '__main__':
    d = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(Solution().calculateMinimumHP2(d))
