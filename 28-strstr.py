class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        if ln > lh:
            return -1
        if needle == "":
            return 0
        for i in range(0, lh-ln+1):
            if haystack[i:i+ln] == needle:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr("hell", "ll"))
