from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先翻再折
        l = len(matrix)
        for i in range(l//2):
            for j in range(l):
                matrix[i][j], matrix[l-i-1][j] = matrix[l-i-1][j], matrix[i][j]
        for i in range(l):
            for j in range(i+1, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #print(matrix)


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    matrix =[
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    Solution().rotate(matrix)
