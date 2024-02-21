class Solution:
    def moveCount(self,target, double):
        if double==0 or target<=2:
            return target-1
        count=1+target%2
        count+=self.moveCount(target//2,double-1)
        return count
    def minMoves(self, target: int, maxDoubles: int) -> int:
        return self.moveCount(target,maxDoubles)