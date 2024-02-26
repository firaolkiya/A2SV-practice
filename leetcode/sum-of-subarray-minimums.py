class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[-1]
        total_sum=0
        for index in range( len(arr)):
            while len(stack)>1 and arr[index]<arr[stack[-1]]:
                ind=stack.pop()
                left=ind-stack[-1]
                right=index-ind
                total_sum+=(left*right*arr[ind])
            stack.append(index)
        while len(stack)>1:
            ind=stack.pop()
            total_sum+=(len(arr)-ind)*(ind-stack[-1])*arr[ind]
        return total_sum%(1000000007)

            
