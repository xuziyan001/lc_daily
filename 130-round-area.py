"""
给你一个 m x n 的矩阵 board ，
由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
"""
from collections import deque
from typing import List

from tool import print_matrix


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        def connect(stack):
            visited = set()
            while stack:
                i, j = stack.popleft()
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    return
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                if board[i+1][j] == 'O':
                    stack.append((i+1,j))
                if board[i][j+1] == 'O':
                    stack.append((i, j+1))
            for i, j in visited:
                board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    d = deque()
                    d.append((i,j))
                    connect(d)


if __name__ == '__main__':
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    Solution().solve(board)
    print_matrix(board)
    board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
    Solution().solve(board)
    print_matrix(board)

