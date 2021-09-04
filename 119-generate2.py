from typing import List

import math


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        newRow = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            newRow[i] = int(math.factorial(rowIndex) / (math.factorial(i)*math.factorial(rowIndex-i)))
        return newRow


if __name__ == '__main__':
    r = Solution().getRow(50)
    print(r)