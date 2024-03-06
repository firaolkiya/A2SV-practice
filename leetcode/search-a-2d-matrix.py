class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        left,right=0,row*col-1

        while left<=right:
            mid=(left+right)//2
            current_row=mid//col
            current_col = mid%col
            if matrix[current_row][current_col]<target:
                left=mid+1
            elif matrix[current_row][current_col]>target:
                right=mid-1
            else:
                return True
        return False


