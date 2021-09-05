"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词


"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        res = []
        def dfs(i, current):
            if s[i:] in wordDict:
                t = current[:]
                t.append(s[i:])
                res.append(' '.join(t))
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    current.append(s[i:j+1])
                    dfs(j+1,current)
                    current.pop()

        dfs(0, [])
        return res


if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))
    print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
    print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    l1 = ["aaaa aa a","aaaa a aa","aa aaaa a","aa aa aa a","aa aa a aa","aa a aaaa","a aaaa aa","a aa aaaa","a a aaaa a","a a aa aa a","a a aa a aa","a a a aaaa"]
    l2 = ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]
    print(len(Solution().wordBreak("aaaaaaa",["aaaa","aa","a"])))
    print(len(l1))
    print(len(l2))

