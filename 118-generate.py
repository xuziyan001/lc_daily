
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def genNext(l):
            if not l:
                return [1]
            if len(l) == 1:
                return [1,1]
            nextRow = [1] * (len(l)+1)
            for i in range(len(l)-1):
                nextRow[i+1] = l[i]+l[i+1]
            return nextRow
        res = []
        start = []
        for i in range(numRows):
            start = genNext(start)
            res.append(start)
        return res


if __name__ == '__main__':
    r = Solution().generate(30)
    print(r)
