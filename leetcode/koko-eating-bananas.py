class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==1:
            return int(ceil(piles[0]/h))
        piles.sort()
        left,right,best = 1,piles[len(piles)-1],0
        

        def getHour(k):
            hour=0
            for i in range(len(piles)):
                hour+=ceil(piles[i]/k)
            return hour
       
        while left<=right:

            mid= (left+right)//2
            requiredHour = getHour(mid)
            if requiredHour<=h:
                right=mid-1
                best=mid
            else: 
                left=mid+1

               
        return best



