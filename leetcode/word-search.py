class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValidIndex(row,col):
            if row<0 or col<0 or row>=len(board) or col>=len(board[0]):
                return False
            return True
        moved= []
        def searchTube(temp_list,row,col,index):
            if index>=len(word):
                return False
            if not isValidIndex(row,col):
                return False
            if board[row][col]!=word[index]:
                return False
            if (row,col) in moved:
                return False
            temp_list.append(board[row][col])
            moved.append((row,col))
            if "".join(temp_list)==word:
                return True
            ##otherwise call the next iteratevley
            if searchTube(temp_list,row-1,col,index+1):
                return True
            elif searchTube(temp_list,row,col+1,index+1):
                return True
            elif searchTube(temp_list,row,col-1,index+1):
                return True
            elif searchTube(temp_list,row+1,col,index+1):
                return True
            else:
                temp_list.pop()
                moved.pop()
                return False
    

        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0]!=board[i][j]:
                    continue
                if searchTube([],i,j,0):
                    return True
               
        return False
        


