from typing import List
"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
"""
"""
给定一个最大矩形，其高为 h， 左边界 l，右边界 r，在矩形的底边，区间 [l, r]内必然存在一点，其上连续1的个数（高度）<=h。若该点存在，
则由于边界内的高度必能容纳h，以上述方法定义的矩形会向上延伸到高度h，再左右扩展到边界 [l, r] ，于是该矩形就是最大矩形。

若不存在这样的点，则由于[l, r]内所有的高度均大于h，可以通过延伸高度来生成更大的矩形，因此该矩形不可能最大。

综上，对于每个点，只需要计算h， l，和 r - 矩形的高，左边界和右边界。
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        max_area = 0
        height = [0] * n
        left = [-1] * n
        right = [n] * n
        for i in range(m):
            for j in range(n):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
            cur_left, cur_right = -1, n
            for j in range(n):
                if matrix[i][j] == '1':
                    # 这里用了上一行的状态，保留了下来
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = -1
                    cur_left = j
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right+1)
                else:
                    right[j] = n
                    cur_right = j-1
            for j in range(n):
                max_area = max(max_area, (right[j]-left[j]-1) * height[j])
        return max_area


if __name__ == '__main__':
    l = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
    print(Solution().maximalRectangle(l))
    l = [["1","0"]]
    print(Solution().maximalRectangle(l))
    l = [["0","0","0"],["0","0","0"],["1","1","1"]]
    print(Solution().maximalRectangle(l))

