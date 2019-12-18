class Solution:
    def reverse(self, x: int) -> int:
        INTMAX = pow(2, 31) - 1
        INTMIN = -pow(2, 31)
        if x == 0:
            return 0
        res = []
        is_pos = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            res.append(x % 10)
            x = x // 10
        rev = 0
        for i in range(len(res)):
            rev *= 10
            rev += res[i]
        if is_pos and rev > INTMAX:
            return 0
        if not is_pos and rev < INTMIN:
            return 0
        return rev * is_pos


if __name__ == '__main__':
    print(Solution().reverse(120))
    print(pow(2, 31))
    print(Solution().reverse(pow(2, 31)))
    print(Solution().reverse(-123))
