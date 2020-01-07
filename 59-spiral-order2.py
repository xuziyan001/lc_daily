from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        starti = 0
        startj = 0
        direct = 'r'
        num = 1
        while True:
            res[starti][startj] = num
            if num == n * n:
                break
            if direct == 'r':
                if startj+1 == n or res[starti][startj+1] != 0:
                    direct = 'd'
                else:
                    startj += 1
                    num += 1
            elif direct == 'l':
                if startj-1 == -1 or res[starti][startj-1] != 0:
                    direct = 'u'
                else:
                    startj -= 1
                    num += 1
            elif direct == 'd':
                if starti+1 == n or res[starti+1][startj] != 0:
                    direct = 'l'
                else:
                    starti += 1
                    num += 1
            else: # u
                if starti-1 == -1 or res[starti-1][startj] != 0:
                    direct = 'r'
                else:
                    starti -= 1
                    num += 1
        return res


if __name__ == '__main__':
    print(Solution().generateMatrix(1))
    print(Solution().generateMatrix(2))
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))
    print(Solution().generateMatrix(5))
