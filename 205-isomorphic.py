class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        t2s = dict()
        s2t = dict()
        for i in range(n):
            if s[i] in s2t:
                if s2t.get(s[i]) != t[i]:
                    return False
            elif t[i] in t2s:
                if t2s.get(t[i]) != s[i]:
                    return False
            else:  # s[i] not in d:
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic("badc","baba"))