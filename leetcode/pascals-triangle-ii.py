class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        array=self.getRow(rowIndex-1)
        current_row=[1]
        for i in range(len(array)-1):
            current_row.append(array[i]+array[i+1])
        current_row.append(1)
        return current_row
