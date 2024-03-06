class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left,right=0,len(nums)-1

        while left<=right:
            mid=(right+left)//2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]<nums[right]:
                right=mid-1
            else:
                left=mid+1
        return -1

            
