"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

"""
import time


class Solution:

    def isMatch2(self, s: str, p: str) -> bool:
        # 贪心算法， 普通DP超时
        if s.count('*') == 0:
            return self.easyMatch(s, p)
        res = []
        for each in p:
            if each == '*' or each == '?':
                if res and res[-1] == '*':
                    continue
            res.append(each)
        p = ''.join(res)
        index = p.find('*')
        rindex = p.find('*')
        if not self.easyMatch(s[:index], p[:index]):
            return False
        if not self.easyMatch(s[rindex+1:], p[len(p)-len(s)+rindex+1:]):
            return False
        s = s[index+1:len(s)-len(p)+rindex]
        p = p[index+1:rindex]
        return self.seq(s, p)

    def easyMatch(self, s, p):
        if len(s) != len(p):
            return False
        for i in range(len(s)):
            if p[i] != '?' and p[i] != s[i]:
                return False
        return True

    def isMatch(self, s: str, p: str) -> bool:
        # group by *
        res = []
        for each in p:
            if each == '*':
                if res and res[-1] == '*':
                    continue
            res.append(each)
        p = ''.join(res)
        lens = len(s) # i
        lenp = len(p) # j
        if lenp == 0:
            return lens == lenp
        dp = [[False] * (lenp+1) for i in range(lens+1)]
        dp[0][0] = True
        dp[0][1] = True if p[0] == "*" else False
        for j in range(2, lenp+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1]
        for i in range(1, lens+1):
            for j in range(1, lenp+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == '?':
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == '*':
                        # 这里是重点！！ 用不着去循环整个行
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    else:
                        dp[i][j] = False
        return dp[lens][lenp]


if __name__ == '__main__':
    s = "aa"
    p = "a"
    print(Solution().isMatch(s, p))
    s = "aa"
    p = "*"
    print(Solution().isMatch(s, p))
    s = "cb"
    p = "?a"
    print(Solution().isMatch(s, p))
    s = "adceb"
    p = "*a*b"
    print(Solution().isMatch(s, p))
    s = "aa"
    p = "a"
    print(Solution().isMatch(s, p))
    s = "acdcb"
    p = "a*c?b"
    print(Solution().isMatch(s, p))
    s = ""
    p = ""
    print(Solution().isMatch(s, p))
    t = time.time()
    s = "aaaababbbabbbbaabbaaabbbbabbbbbabaaaabbbbbaaaabbbbbaaabbaaaabbabbabbabababaabbbbaabaaabbabbaabbababbbabbbbbaaabaaaababababbaaaabaabaaabbbbbbbbbabbbaabbaaaaaabbabaabaaabbbaaabaaabaaabaabbabaabbaaabaaabb"
    p = "bb*****b*ba*a**bb*b**aba**a*b*b*b*a*b*a*ba*b*a*a*****a*b***a*a**a**b**b***a*a***bbba*abb*abba*bab***"
    print(Solution().isMatch(s, p))
    print(time.time()-t)
    t = time.time()
    s = "bababababababaaaababbabbbbabbbaabbbabaaaaaababbbababbbaaaaabbaaabbaabaababbbaaaaaabbbbabbabaababaabbabababaaaaaaabbbababbbbbabaabbbababbbbabbabbabaaaaaaabbabababaaaabaaaabbabaaaababbabaabbaaabbaabaabaabaa"
    p = "a*bab*******b*******babb*ba*aa*a*aa***bbbaa***b**aaaabb**bb*ba*aa***bb**baba********a***b*b*a**a******ba"
    print(Solution().isMatch(s, p))
    print(time.time()-t)
