class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1
        t = abs(n)
        x = 1/x if n < 0 else x
        res = x
        for i in range(1, t):
            res *= x
            if res == 0:
                return 0
        return res


if __name__ == '__main__':
    print(Solution().myPow(2.2, 10))
    print(Solution().myPow(2.0, -2))
    print(Solution().myPow(0.00001,2147483647))
