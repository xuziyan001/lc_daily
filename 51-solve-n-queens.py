from typing import List


class Solution:

    def __init__(self):
        self.res = []
        self.init = -pow(2, 28)

    def solveNQueens(self, n: int) -> List[List[str]]:
        a = [self.init for i in range(n)] #一维数组表示棋盘
        i, j = 0, 0
        while i < n:
            while j < n:
                if self.valid(a, i, j):
                    a[i] = j
                    j = 0
                    break
                else:
                    j += 1
            if a[i] == self.init:
                # 第i行没有找到可以放置皇后的位置
                if i == 0:
                    break
                else:
                    i -= 1
                    j = a[i] + 1  # 这里是回溯的核心，上一行不取第一个可取值，而是向后继续
                    a[i] = self.init
                    continue
            if i == n-1:
                # 找到了一种解法
                self.construct(a)
                j = a[i] + 1
                a[i] = self.init
                continue
            i += 1
        return self.res

    def valid(self, a, row, col):
        for i in range(len(a)):
            if a[i] == col or abs(i-row) == abs(a[i]-col):
                return False
        return True

    def construct(self, a):
        r = [['.'] * len(a) for i in range(len(a))]
        for i in range(len(a)):
            r[i][a[i]] = 'Q'
        self.res.append([''.join(l) for l in r])


if __name__ == '__main__':
    l = Solution().solveNQueens(12)
    for ll in l:
        for lll in ll:
            pass
            #print(lll)
        #print('-'*100)
    print(len(l))
