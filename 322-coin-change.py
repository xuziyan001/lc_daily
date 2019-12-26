from typing import List


class Solution:

    def __init__(self):
        self.memo = dict()

    def coinChange1(self, coins: List[int], amount: int) -> int:
        #   #5超时
        mins = []
        coins.sort(reverse=True)
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        for each in coins:
            target = amount - each
            if target in self.memo:
                min1 = self.memo[target]
            else:
                min1 = self.coinChange(coins, target)
                if min1 == -1:
                    continue
                self.memo[target] = min1
            mins.append(min1)
        if len(mins) == 0:
            return -1
        all_min = min(mins) + 1
        return all_min

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(coins[0], amount+1):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i-coin] + 1, dp[i])
        return -1 if dp[amount] > amount else dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))
    print(Solution().coinChange([3,7,405,436], 8839))
    print(Solution().coinChange([2,5,10,1], 27))
    print(Solution().coinChange([186,419,83,408], 6249))
