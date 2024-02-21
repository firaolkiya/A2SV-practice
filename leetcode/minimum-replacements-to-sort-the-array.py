class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        right=nums[len(nums)-1]
        left=len(nums)-2
        count=0
         
        while left>=0:
            if nums[left]>right:
                n=ceil(nums[left]/right)
                count+=n-1
                right=(nums[left])//n
            else:
                right=nums[left]
            left-=1   
        return count      


