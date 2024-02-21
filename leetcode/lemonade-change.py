class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money=defaultdict(int)
        for bill in bills:
            if bill==10:
                if money[5]==0:
                    return False
                else:
                    money[5]-=1
            elif bill==20:
                if money[10]>0 and money[5]>0:
                    money[5]-=1
                    money[10]-=1
                elif money[5]>2:
                    money[5]-=3
                else:
                    return False
            money[bill]+=1
            
        return True