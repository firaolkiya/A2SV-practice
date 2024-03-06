class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def youtube1():
            left,right=0, len(nums)-1
            start=-1
            while left<=right:
                mid=(right+left)//2
                if nums[mid]==target:
                    start=mid
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return start
            
        def youtube2():
            left,right=0, len(nums)-1
            end=-1
            while left<=right:
                mid=(right+left)//2
                if nums[mid]==target:
                    end=mid
                if nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return end
        return [youtube1(),youtube2()]
            
        
        


            
