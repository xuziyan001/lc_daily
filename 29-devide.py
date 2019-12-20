class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            return pow(2, 31) - 1 # overflow1
        is_neg = 1
        if dividend > 0 > divisor or divisor > 0 > dividend:
            is_neg = -1
        result = 0
        if dividend == -pow(2, 31):
            if divisor > 0:
                if divisor == 1:
                    return dividend
                else:
                    dividend += divisor
                    result += 1
            else:
                if divisor == -1:
                    return pow(2, 31) - 1 # overflow2
                dividend -= divisor
                result += 1
        if divisor == -pow(2, 31):
            return result * is_neg
        dividend = abs(dividend)
        divisor = abs(divisor)
        remain = dividend
        div = 0
        while dividend >= (divisor << div):
            div += 1
        if div == 0:
            return result * is_neg
        while div >= 1:
            div -= 1
            if remain >= (divisor << div):
                remain -= (divisor << div)
                result += pow(2, div)
            else:
                continue
        return result * is_neg


if __name__ == '__main__':
    print(Solution().divide(10, 3))
    print(Solution().divide(20, 3))
    print(Solution().divide(-20, 3))
    print(Solution().divide(-200, 300))
    print(Solution().divide(-20000988, 312))
    print(Solution().divide(-2147483648, 1))
    print(Solution().divide(-2147483648, 2))
    print(Solution().divide(2147483647, 3))
    print(Solution().divide(1, 1))
    print(Solution().divide(-2147483648, -1109186033))


