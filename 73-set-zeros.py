from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        S = pow(2, 31)
        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        if n == 0:
            return None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    continue
                else:
                    for t in range(m):
                        if matrix[t][j] != 0:
                            matrix[t][j] = S
                    for t in range(n):
                        if matrix[i][t] != 0:
                            matrix[i][t] = S
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == S:
                    matrix[i][j] = 0


if __name__ == '__main__':
    l = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    Solution().setZeroes(l)
    print(l)