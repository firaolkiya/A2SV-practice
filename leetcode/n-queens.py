class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiagonal = set()
        negDiagonal = set()
        column = set()
        ans=[]
        chessBoard = [["."]*n for i in range(n)]
        isCheckmate = lambda row, col: (row + col) in posDiagonal or (row - col) in negDiagonal or col in column
        def validateBoard(row):
            if row==n:
                row_content=["".join(r_th) for r_th in chessBoard]
                ans.append(row_content)
                return
            
            for row_col in range(n):
                if isCheckmate(row,row_col):
                    continue
                column.add(row_col)
                negDiagonal.add(row-row_col)
                posDiagonal.add(row+row_col)
                chessBoard[row][row_col]="Q"

                validateBoard(row+1)
                column.remove(row_col)
                negDiagonal.remove(row-row_col)
                posDiagonal.remove(row+row_col)
                chessBoard[row][row_col]="."
        validateBoard(0)
        return ans




