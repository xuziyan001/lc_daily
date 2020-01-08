class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        left = 1
        right = x // 2 + 1
        while left < right:
            mid = (left+right) >> 1
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == '__main__':
    print(Solution().mySqrt(9))
    print(Solution().mySqrt(22334239842309)) # 4725911
