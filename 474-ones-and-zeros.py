from typing import List


"""
在计算机界中，我们总是追求用有限的资源获取最大的收益。

现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。

你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
"""


"""
核心思路是准备多个背包，然后对列表中的每个字符串进行取舍；
注意由于每个字符串只能使用一次（即有限背包），因此在更新 dp(i, j) 时，i 和 j 都需要从大到小进行枚举。
因为一轮迭代的背包缩容的过程中，小容量背包不可能包含当前资源；

无限背包的情况下，需要从小到大枚举。因为在背包容量扩大的过程中，有可能就某一资源进行了多次装载：
（dp[i-zeros][j-ones] + 1）的情况下前一个小背包有可能已经装过该资源了；

"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for i in range(m+1)]
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    if zeros > i or ones > j:
                        dp[i][j] = dp[i][j]
                    else:
                        dp[i][j] = max(dp[i-zeros][j-ones] + 1, dp[i][j])
        return dp[m][n]


if __name__ == '__main__':
    print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
    print(Solution().findMaxForm(["10", "0", "1"], 1, 1))
