"""
Problem Description
一个正整数N(0＜ｎ＜100），可以写成若干个正整数加数之和，如6可以写成

6=1+2+3；
6=2+2+2；
6=2+4；
6=3+3；
6=1+5；
……

其中有一种分解方式获得的加数的乘积是所有分解方式中最大的，比如上面分解中最大的乘积是3×3＝9。

请你设计一种算法，对于任何一个输入的正整数，求出其各种分解中所得到的最大乘积。

Input

输入有多组，每组一行输入一个正整数。以0作为输入的结束。

Output

对应输入的数据，输出多行，输出所求最大分解乘积。 保证答案在64位整数以内 .
"""

class Solution:
    def getMax(self, n):
        if n <= 4:
            return n
        dp = list(range(n+1))
        for i in range(5, n+1):
            current_max = i
            for j in range(1, i):
                current_max = max(dp[j] * (i-j), current_max)
            dp[i] = current_max
        return dp[n]

    def getMaxTrue(self, n):
        if n <= 4:
            return n
        return self.getMaxTrue(n-3) * 3

if __name__ == "__main__":
    print(Solution().getMax(11))
    print(Solution().getMaxTrue(11))
