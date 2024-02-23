class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opens={"[":"]","{":"}","(":")"}
        for i in s:
            if i in opens:
                stack.append(i)
            elif stack and opens[stack[-1]]==i:
                stack.pop()
            else:
                return False
                
        return  len(stack)==0