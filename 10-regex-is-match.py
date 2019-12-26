class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens = len(s) # i
        lenp = len(p) # j
        if lenp == 0:
            return lens == lenp
        dp = [[False] * (lenp+1) for i in range(lens+1)]
        dp[0][0] = True
        dp[0][1] = True if p[0] == "*" else False
        for j in range(2, lenp+1):
            if j == 2 and p[j-1] == "*":
                dp[0][j] = True
                continue
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1] or dp[0][j-2]
        for i in range(1, lens+1):
            for j in range(1, lenp+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == '*':
                        if j < 2:
                            dp[i][j] = False
                            continue
                        if p[j-2] == '.' or p[j-2] == s[i-1]:
                            dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
                        elif p[j-2] != s[i-1]:
                            dp[i][j] = dp[i][j-2]
                        else:
                            dp[i][j] = False
                    else:
                        dp[i][j] = False
        return dp[lens][lenp]


if __name__ == '__main__':
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa", "a*"))
    print(Solution().isMatch("ab", ".*"))
    print(Solution().isMatch("aab", "c*a*b"))
    print(Solution().isMatch("a", ""))
    print(Solution().isMatch("", "c*c*"))
