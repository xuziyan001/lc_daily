class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        remains = self.sub(s3, s1, 0, 0, '')
        return s2 in remains

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
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(Solution().isInterleave(s1,s2,s3))
    s1= "cabbacccabacbcaabaccacacc"
    s2="bccacbacabbabaaacbbbbcbbcacc"
    s3="cbccacabbacabbbaacbcacaaacbbacbcaabbbbacbcbcacccacacc"
    l = Solution().sub(s3,s1,0,0,'')
    print(len(l))

