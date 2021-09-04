

"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

"""
from typing import List

import sys


class Solution:
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        self.min = sys.maxsize
        def recur(level, index, currentSum):
            if level >= len(triangle):
                if currentSum < self.min:
                    self.min = currentSum
                return
            if index >= len(triangle[level]):
                return
            currentSum += triangle[level][index]
            recur(level+1, index, currentSum)
            recur(level+1, index+1, currentSum)
        recur(0, 0, 0)
        return self.min

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    r = Solution().minimumTotal(triangle)
    print(r)
    triangle = [[-10]]
    r = Solution().minimumTotal(triangle)
    print(r)

