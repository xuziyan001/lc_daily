from typing import List
from functools import reduce


class Solution:
    def __init__(self):
        self.res = []
        self.k = 0

    def dfs(self, current: List[int], remain: List[int]) -> str:
        if not remain:
            self.res.append(current)
            if len(self.res) == self.k:
                return ''.join(map(str, current))
        for each in remain:
            t = current.copy()
            t.append(each)
            tt = remain.copy()
            tt.remove(each)
            s = self.dfs(t, tt)
            if s:
                return s

    def getPermutation2(self, n: int, k: int) -> str:
        r = list(range(1, n+1))
        self.k = k
        return self.dfs([], r)

    def getPermutation(self, n: int, k: int) -> str:
        r = list(range(1, n+1))
        result = []
        t = n-1
        while k:
            d, m = divmod(k, self.factorial(t))
            if m != 0:
                k = m
                num = r[d]
                result.append(num)
                r.remove(num)
                t -= 1
            else:
                k = m
                num = r[d-1]
                result.append(num)
                r.remove(num)
                r.reverse()
        result += r
        return ''.join(map(str, result))

    def factorial(self, n: int) -> int:
        if n < 2:
            return 1
        return reduce(lambda x,y:x*y, range(1,n+1),1)


if __name__ == '__main__':
    print(Solution().getPermutation(3,3))
    print(Solution().getPermutation(4,9))
    print(Solution().getPermutation(9,135401))
