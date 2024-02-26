class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       stack=[]
       array=[0]*len(temperatures)
       for i, temp in enumerate(temperatures):
           while stack and temp>temperatures[stack[-1]]:
               array[stack[-1]]=i-stack[-1]
               stack.pop()
           stack.append(i)
       return array
            