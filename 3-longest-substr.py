

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start = 0
        end = 1
        length = 0
        cl = 1
        while end != len(s):
            if s[end] not in s[start:end]:
                end += 1
                cl = end - start
            else:
                # 这里的重点在于回溯，找到上一个相同字符所在的位置，并将其下一个位置作为起始
                start = s.index(s[end], start, end)+1
                if cl > length:
                    length = cl
        if cl > length:
            length = cl
        return length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))
    print(Solution().lengthOfLongestSubstring('bbbbbb'))
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring(''))
    print(Solution().lengthOfLongestSubstring('a'))
    print(Solution().lengthOfLongestSubstring('ab'))
    print(Solution().lengthOfLongestSubstring('dvdf')) #3
