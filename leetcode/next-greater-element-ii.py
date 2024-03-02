class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answ=[-1]*len(nums)
        stack = deque()
        for index,num in enumerate(nums):
            while stack and nums[stack[-1]]<num:
                temp=stack.pop()
                answ[temp]=num
            stack.append(index)
        for index,num in enumerate(nums):
            if not stack:
                break
            while stack and nums[stack[-1]]<num:
                temp=stack.pop()
                if answ[temp]==-1:
                    answ[temp]=num
            if index>=stack[-1]:
                stack.pop()
        return answ