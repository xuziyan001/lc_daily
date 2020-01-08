from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        i = 0
        j = n-1
        while i < m:
            if matrix[i][0] <= target <= matrix[i][j]:
                break
            i += 1
        if i == m:
            return False
        return target in matrix[i]


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print(Solution().searchMatrix(matrix, target))
