from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [int(x,2) for x in self.gen_code(n)]

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
