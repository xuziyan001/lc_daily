"""

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        min_buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            if prices[i] - min_buy > profit:
                profit = prices[i] - min_buy
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))
