class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        palin = 0
        while tmp != 0:
            palin *= 10
            palin += tmp % 10
            tmp //= 10
        return x == palin


if __name__ == '__main__':
    print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(-11))
