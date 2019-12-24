from typing import List
import copy


class Solution:
    def isValidSudokuForAnswer(self, board: List[List[str]]):
        l = 9
        for i in range(l):
            for j in range(l):
                if board[i][j] == ".":
                    # search row
                    remains = [str(t) for t in range(1, 10)]
                    for k in range(l):
                        current = board[i][k]
                        if current != ".":
                            if current not in remains:
                                continue
                            else:
                                remains.remove(current)
                    # search col
                    for k in range(l):
                        current = board[k][j]
                        if current != ".":
                            if current not in remains:
                                continue
                            else:
                                remains.remove(current)
                    # search block
                    di = i // 3
                    dj = j // 3
                    for m in range(3):
                        for n in range(3):
                            current = board[3*di+m][3*dj+n]
                            if current != ".":
                                if current not in remains:
                                    continue
                                else:
                                    remains.remove(current)
                    if not remains:
                        return False
                    for each in remains:
                        nextb = copy.deepcopy(board)
                        # nextb = copy.copy(board)
                        nextb[i][j] = each
                        is_valid = self.isValidSudokuForAnswer(nextb)
                        if is_valid:
                            return is_valid
                    return False
                else:
                    continue
        return board

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        s = self.isValidSudokuForAnswer(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = s[i][j]


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(Solution().solveSudoku(board))
    print(board)
