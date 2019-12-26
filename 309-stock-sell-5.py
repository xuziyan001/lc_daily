from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp_0, dp_1 = 0, 0
        n = len(prices)
        dp_pre = 0  # 存储前天不持有的最大收益
        for i in range(n):
            if i == 0:
                dp_0 = 0
                dp_1 = -prices[0]
                continue
            tmp = dp_0
            dp_0 = max(dp_0, dp_1+prices[i])
            dp_1 = max(dp_pre-prices[i], dp_1)
            dp_pre = tmp
        return dp_0


if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,0,2]))
