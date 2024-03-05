class Solution:
    def isValid(self,s):
        stack=[]
        for ch in s:
            if stack and stack[-1]=="(" and ch==")":
                stack.pop()
            else:
                stack.append(ch)          
        return len(stack)==0
    def generateParenthesis(self, n: int) -> List[str]:
        validatedBracket = []
        bracket = ["(",")"]
        def validate(temp_list,k):
            if k==2*n:
                if self.isValid(temp_list) and temp_list not in validatedBracket:
                    validatedBracket.append("".join(temp_list))
                return
            for bra in bracket:
                temp_list.append(bra)
                validate(temp_list,k+1)
                temp_list.pop()
        validate([],0)
        return validatedBracket