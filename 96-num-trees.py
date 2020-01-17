"""
这里利用动态规划思想，选举一个根并把序列按照左右子树分开，左右子树的组个个数乘积就是当前选举根的组合个数
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
