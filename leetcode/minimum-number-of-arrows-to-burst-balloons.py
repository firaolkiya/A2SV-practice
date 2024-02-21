class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev=points[0][1]
        count=1
        for point in points:
            if point[0]>prev:
                count+=1
                prev=point[1]
            else:
                prev=min(prev,point[1])
        return count
