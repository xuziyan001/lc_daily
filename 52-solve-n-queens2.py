
class Solution:

    def __init__(self):
        self.res = 0
        self.init = -pow(2, 28)

    def totalNQueens(self, n: int) -> int:
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
                self.res += 1
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


if __name__ == '__main__':
    l = Solution().totalNQueens(11)
    print(l)
