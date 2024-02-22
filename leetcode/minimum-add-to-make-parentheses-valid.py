class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closed=0
        opened=0
        for i in s:
            if i=="(":
                opened+=1
            else:
                if opened>0:
                    opened-=1
                else:
                    closed+=1
        return opened+closed