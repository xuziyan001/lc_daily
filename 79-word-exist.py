"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

"""

"""
dfs
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word[1:], [(i,j)]):
                        return True
        return False

    def dfs(self, board, word, stack):
        if not word:
            return True
        i, j = stack[-1]
        if i-1 >= 0 and (i-1, j) not in stack and board[i-1][j] == word[0]:
            s = stack[:]
            s.append((i-1, j))
            if self.dfs(board, word[1:], s):
                return True
        if i+1 < len(board) and (i+1, j) not in stack and board[i+1][j] == word[0]:
            s = stack[:]
            s.append((i+1, j))
            if self.dfs(board, word[1:], s):
                return True
        if j-1 >= 0 and (i, j-1) not in stack and board[i][j-1] == word[0]:
            s = stack[:]
            s.append((i, j-1))
            if self.dfs(board, word[1:], s):
                return True
        if j+1 < len(board[0]) and (i, j+1) not in stack and board[i][j+1] == word[0]:
            s = stack[:]
            s.append((i, j+1))
            if self.dfs(board, word[1:], s):
                return True
        return False


if __name__ == '__main__':
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))
    word = "ABCB"
    print(Solution().exist(board, word))
    word = "SEE"
    print(Solution().exist(board, word))
    word = "ABCECBA"
    print(Solution().exist(board, word))


