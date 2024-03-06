class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def checker(radius):
            index=0
            h_index=0
            while index<len(houses):
                if h_index>=len(heaters):
                    return False
                if abs(houses[index]-heaters[h_index])>radius:
                    h_index+=1
                else:
                    index+=1
            return True
        
        left,right,best=0,max(heaters[-1]-houses[0],houses[-1]-heaters[0]),0
 
        while left<=right:
            mid = (left+right)//2
            if checker(mid):
                best=mid
                right=mid-1
            else:
                left=mid+1
        return best



