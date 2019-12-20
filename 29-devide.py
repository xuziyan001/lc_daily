class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        is_neg = 1
        if dividend > 0 > divisor or divisor > 0 > dividend:
            is_neg = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        remain = dividend
        div = 1
        result = 0
        while remain >= divisor:

