from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        dp_0, dp_1 = 0, 0
        n = len(prices)
        for i in range(n):
            if i == 0:
                dp_0 = 0
                dp_1 = -prices[0]
                continue
            tmp = dp_0
            dp_0 = max(dp_0, dp_1+prices[i]-fee)
            dp_1 = max(tmp-prices[i], dp_1)
        return dp_0


if __name__ == '__main__':
    l = [1, 3, 2, 8, 4, 9]
    print(Solution().maxProfit(l, 2))
