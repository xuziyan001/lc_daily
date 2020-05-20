"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
"""
"""
这里明显可以用动态规划的思想解决
dp(i,j)代表s1的前i位，s2的前j位，与s3的前i+j位的匹配关系
dp（i+1，j） = dp（i，j） and s3[i+j+1] == s1[i+1] 或者 dp（i+1，j-1） and s3[i+j+1] == s2[j]
dp（i，j+1）同理
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            dp[i][0] = (s1[:i] == s3[:i])
        for j in range(n+1):
            dp[0][j] = (s2[:j] == s3[:j])
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i+j-1]:
                    if s2[j-1] == s3[i+j-1]:
                        dp[i][j] = dp[i-1][j] | dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-1][j]
                elif s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[m][n]

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        remains = self.sub(s3, s1, 0, 0, '')
        return s2 in remains

    # This is wrong answer
    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        i, j = 0, 0
        while i != m:
            if s1[i] == s3[j]:
                i += 1
                s3 = s3[:j] + s3[j+1:]
            else:
                j += 1
            if j >= m+n:
                return False
        return s3 == s2

    def sub(self, s1, s2, i, j, remains):
        m = len(s1)
        n = len(s2)
        if i == m and j == n:
            return [remains]
        if i >= m:
            return []
        if j >= n:
            return [remains+s1[i:]]
        if m-i < n-j:
            return []
        if s1[i] != s2[j]:
            return self.sub(s1, s2, i+1, j, remains+s1[i])
        else:
            not_get = self.sub(s1, s2, i+1, j, remains+s1[i])
            get = self.sub(s1, s2, i+1, j+1, remains)
            return not_get + get


if __name__ == '__main__':
    s1 = "adcad"
    s2 = "ad"
    print(Solution().sub(s1,s2,0,0,''))
    s1 = "aadbbcbcac"
    s2 = "aabcc"
    print(Solution().sub(s1,s2,0,0,''))
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1,s2,s3))
    print(Solution().isInterleave3(s1,s2,s3))
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(Solution().isInterleave(s1,s2,s3))
    print(Solution().isInterleave3(s1,s2,s3))
    s1= "cabbacccabacbcaabaccacacc"
    s2="bccacbacabbabaaacbbbbcbbcacc"
    s3="cbccacabbacabbbaacbcacaaacbbacbcaabbbbacbcbcacccacacc"
    print(Solution().isInterleave(s1,s2,s3))
    print(Solution().isInterleave3(s1,s2,s3))

