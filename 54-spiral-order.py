from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        if rows == 0:
            return self.res
        if rows == 1:
            self.res += matrix[0]
            return self.res
        cols = len(matrix[0])
        if cols == 0:
            return self.res
        if cols == 1:
            for each in range(rows):
                self.res.append(matrix[each][0])
            return self.res
        self.res += matrix[0]
        for each in range(1, rows-1):
            self.res.append(matrix[each][-1])
        l = matrix[-1].copy()
        l.reverse()
        self.res += l
        for each in range(rows-2, 0, -1):
            self.res.append(matrix[each][0])
        for i in range(rows):
            matrix[i] = matrix[i][1:-1]
        matrix = matrix[1:-1]
        return self.spiralOrder(matrix)


if __name__ == '__main__':
    l = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
    print(Solution().spiralOrder(l))
    l = [[3],[2]]
    print(Solution().spiralOrder(l))

