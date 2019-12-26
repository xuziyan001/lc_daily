from typing import List

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        i = 0
        while i < len(prices)-1:
            j = i + 1
            if prices[j] < prices[i]:
                i = j
            else:
                while j+1 < len(prices):
                    if prices[j+1] >= prices[j]:
                        j += 1
                    else:
                        break
                profit += prices[j] - prices[i]
                i = j+1
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([1,2,3,4,5]))

