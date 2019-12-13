class Solution:
    def longestPalindromeV1(self, s: str) -> str:
        if len(s) < 2:
            return s
        result = [0] * len(s)
        result[0] = 1
        r = s[0]
        for i in range(1, len(s)):
            last_max = result[i-1]
            for j in range(0, i-last_max+1):
                sl = s[j:i+1]
                if is_p(sl):
                    result[i] = i+1-j
                    r = sl
                    break
                else:
                    continue
            if result[i] == 0:
                result[i] = last_max
        return r

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        result = [0] * len(s)
        result[0] = 1
        r = s[0]
        for i in range(1, len(s)):
            max_len = result[i-1]
            if i-1-max_len >= 0 and is_p(s[i-1-max_len:i+1]):
                result[i] = max_len + 2
                r = s[i-1-max_len:i+1]
                continue
            if i-max_len >= 0 and is_p(s[i-max_len:i+1]):
                result[i] = max_len + 1
                r = s[i-max_len:i+1]
            else:
                result[i] = max_len
        return r


def is_p(s: str) -> bool:
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-1-i]:
            return False
    return True


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("asdddsa"))
    print(Solution().longestPalindrome(""))
    print(Solution().longestPalindrome("ac"))
    print(Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
