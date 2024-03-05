from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        validPosition = lambda row, col: 0 <= row < 9 and 0 <= col < 9
        
        def isValid(row, col):
            for i in range(9):
                if i != col and board[row][i] == board[row][col]:
                    return False
            for i in range(9):
                if i != row and board[i][col] == board[row][col]:
                    return False
            ceilR = row // 3 * 3
            ceilC = col // 3 * 3
            temp = set()
            for i in range(ceilR, ceilR + 3):
                for j in range(ceilC, ceilC + 3):
                    if board[i][j] in temp and board[i][j] != ".":
                        return False
                    temp.add(board[i][j])
            return True

        def gamePlayer(colAndRow):
            if colAndRow == 81:
                return True
            row = colAndRow // 9
            col = colAndRow % 9
            if board[row][col] != ".":
                return gamePlayer(colAndRow + 1)
            for i in range(1, 10):
                board[row][col] = str(i)
                if isValid(row, col) and gamePlayer(colAndRow + 1):
                    return True
                board[row][col] = "."
            return False

        gamePlayer(0)
        return board
