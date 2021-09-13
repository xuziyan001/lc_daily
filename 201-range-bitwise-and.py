# 给你两个整数 left 和 right ，表示区间 [left, right] ，
# 返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
from math import log2


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left <= 0 or left > right:
            return 0
        x = left
        q = int(log2(left))
        end = int(pow(2,q+1))
        if end <= right:
            return 0
        start = left
        while start <= right:
            x &= start
            if x:
                start += 1
            else:
                start = end
        return x


if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(600000000,2147483645))