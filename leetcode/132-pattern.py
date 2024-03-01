class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack =[]
        min_value=float('-inf')
        for num in reversed(nums):
            if num<min_value:
                return True
            while  stack and num>stack[-1]:
                min_value=max(min_value,stack[-1])
                stack.pop()
            stack.append(num)
        return False
            
