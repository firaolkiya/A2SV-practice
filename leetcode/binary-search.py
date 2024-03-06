class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def searchTube(left,right):
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            if left>right:
                return -1
            if target<nums[mid]:
                return searchTube(left,mid-1)
            return searchTube(mid+1,right)
        return searchTube(0,len(nums)-1)