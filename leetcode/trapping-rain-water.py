class Solution:
    def trap(self, height: List[int]) -> int:
        stored_water=0
        stack=[]
        for index,num in enumerate(height):
            while stack and height[stack[-1]]<num:
                short=height[stack.pop()]
                if stack:
                    longs=min(num,height[stack[-1]])
                    stored_water+=(longs-short)*(index-stack[-1]-1)
            stack.append(index)
        return stored_water
               
        