class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operator="+-*/" 
        for char in tokens:
            if char in operator:
               first_operand=stack.pop()
               second_operand=stack.pop()
               result=int(eval(second_operand+char+first_operand))
               stack.append(str(result))
            else:
                stack.append(char)
        return int(stack[0])