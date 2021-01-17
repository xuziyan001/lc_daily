"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            return 0 if s != t else 1
        ls = len(s)
        lt = len(t)
        result = [[0] * (ls+1) for i in range(lt+1)]
        for j in range(1, ls+1):
            result[1][j] = s[:j].count(t[0])
        for i in range(2, lt+1):
            for j in range(1, ls+1):
                if i == j and t[:i] == s[:j]:
                    result[i][j] = 1
                    continue
                if t[i-1] != s[j-1]:
                    # j-1没有用
                    result[i][j] = result[i][j-1]
                else:
                    # j-1有用&j-1没用
                    result[i][j] = result[i-1][j-1] + result[i][j-1]
        return result[lt][ls]


if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct("rabbbit", "rabbit"))
    print(s.numDistinct("babgba", "ba"))
    print(s.numDistinct("babgbag", "bag"))

