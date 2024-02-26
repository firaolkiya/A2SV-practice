class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for char in s:
            if char=="(":
                stack.append("(")
            elif stack[-1]=="(":
                stack.pop()
                stack.append(1)
            else:
                score_sum=0
                while stack[-1]!="(":
                    score_sum+=stack.pop()
                stack.pop()
                stack.append(score_sum*2)
        return sum(stack)   
        
