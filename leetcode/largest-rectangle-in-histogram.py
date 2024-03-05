class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        area=0
        for h in range(len(heights)):
            while len(stack)>1 and heights[stack[-1]]>heights[h]:
                index=stack.pop()
                leng=h-stack[-1]-1
                area=max(area,(leng)*heights[index])
            stack.append(h)
        while len(stack)>1:
                index=stack.pop()
                leng=len(heights)-stack[-1]-1
                area=max(area,(leng)*heights[index])
        return area
