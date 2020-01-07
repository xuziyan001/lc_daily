class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        res = 0
        for each in s:
            if each == ' ':
                res = 0
            else:
                res += 1
        return res
