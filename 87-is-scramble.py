"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
"""
from functools import lru_cache


class Solution:

    @lru_cache(maxsize=1024)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            # 第一种情况，切割两个子串，并判断两个子串是否可以通过转化得到
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            # 第二种情况，切割并*交换*两个子串进行判断
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


if __name__ == '__main__':
    s1="great"
    s2="rgeat"
    print(Solution().isScramble(s1, s2))
    s1 = "abcde"
    s2 = "caebd"
    print(Solution().isScramble(s1, s2))

