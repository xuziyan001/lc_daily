

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while j > i:
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
