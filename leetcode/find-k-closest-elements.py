class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left,right,midIndex = 0,len(arr)-1,0

        while left<=right:
            mid= left+(right-left)//2
            if abs(arr[mid]-x)<abs(arr[midIndex]-x):
                midIndex=mid
            if arr[mid]>x:
                right=mid-1
            elif arr[mid]<x:
                left=mid+1
            else:
                break
        left=midIndex-1
        right=midIndex
        ans=[]
        for i in range(k):
            if left>=0 and right<len(arr):
                if abs(arr[left]-x)<=abs(arr[right]-x):
                    ans.append(arr[left])
                    left-=1
                else:
                    ans.append(arr[right])
                    right+=1
            elif left>=0:
                ans.append(arr[left])
                left-=1
            else:
                ans.append(arr[right])
                right+=1
        return sorted(ans)






