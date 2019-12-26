from typing import List

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        if k > n//2:
            # TODO 退化到无数次
            return self.maxProfitUnlimit(prices)
        max_k = k
        dp = [[[0]*2 for i in range(max_k+1)] for j in range(n)]
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i-1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[n-1][max_k][0]

    def maxProfitUnlimit(self, prices: List[int]) -> int:
        dp_0, dp_1 = 0, 0
        n = len(prices)
        for i in range(n):
            if i == 0:
                dp_0 = 0
                dp_1 = -prices[0]
                continue
            tmp = dp_0
            dp_0 = max(dp_0, dp_1+prices[i])
            dp_1 = max(tmp-prices[i], dp_1)
        return dp_0


if __name__ == '__main__':
    l = [3, 3, 5, 0, 0, 3, 1, 4]
    print(Solution().maxProfit(2,l))
    print(Solution().maxProfit(100,l))
    l = [1,2,3,4,5]
    print(Solution().maxProfit(2,l))
    l = [7,6,4,3,1]
    print(Solution().maxProfit(2,l))
