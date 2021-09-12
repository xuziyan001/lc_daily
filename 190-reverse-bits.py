# 颠倒给定的 32 位无符号整数的二进制位。

class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)

        length = len(b)-2

        x = 0
        bi = 31
        ti = 1
        for i in range(length-1, -1, -1):
            if bi > 0:
                x += (ti&n) << bi
            else:
                x += (ti&n) >> -bi
            print(bin(x))
            bi -= 2
            ti = ti << 1

        return x


if __name__ == '__main__':
    print(Solution().reverseBits(0b00000010100101000001111010011100))
    #print(Solution().reverseBits(4294967296))