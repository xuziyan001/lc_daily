class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [1] * (len(s)+1)
        for i in range(2, len(s)+1):
            current = s[i-1]
            pre = s[i-2]
            if current == '0':
                if pre in ('1', '2'):
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if pre == '0':
                    dp[i] = dp[i-1]
                else:
                    if int(pre+current) <= 26:
                        dp[i] = dp[i-1]+dp[i-2]
                    else:
                        dp[i] = dp[i-1]
        return dp[len(s)]


if __name__ == '__main__':
    print(Solution().numDecodings("12"))
    print(Solution().numDecodings("10"))
    print(Solution().numDecodings("100"))
    print(Solution().numDecodings("110"))
    print(Solution().numDecodings("10032"))
    print(Solution().numDecodings("0"))
    print(Solution().numDecodings("226"))
    print(Solution().numDecodings("1212"))
