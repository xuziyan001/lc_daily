"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，
判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        """
        self.found = False
        def dfs(i):
            if s[i:] in wordDict:
                self.found = True
                return True
            for j in range(n-1, i-1, -1):
                if s[i:j+1] in wordDict:
                    if dfs(j+1):
                        break
        dfs(0)
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))
    print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
    print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
