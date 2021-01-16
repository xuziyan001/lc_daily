"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。

格雷编码序列必须以 0 开头。
"""
"""
这里有一个取巧，即当第i位确定的时候，剩余的位数只需要二分反序就可以了
如：
f(2) = 
00
01
10
11
f(3) = 
000
001
011
010
110
111
101
100
这里可以看到 f(3) = "0+f(2)" + "1+~f(2)"
"""


from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [int(x, 2) for x in self.gen_code(n)]

    def gen_code(self, n):
        if n == 0:
            return ['0']
        if n == 1:
            return ['0', '1']
        t = self.gen_code(n-1)
        t2 = t.copy()
        t2.reverse()
        return ['0'+x for x in t] + ['1'+x for x in t2]


if __name__ == '__main__':
    print(Solution().grayCode(0))
    print(Solution().grayCode(1))
    print(Solution().grayCode(2))
    print(Solution().grayCode(3))
    print(Solution().grayCode(4))
    print(Solution().grayCode(5))
