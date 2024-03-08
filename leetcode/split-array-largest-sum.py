class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:


        def part(sum_):
            temp=1
            runningSum=0
            for i in range(len(nums)):
                runningSum+=nums[i]
                if runningSum>sum_:
                    runningSum=nums[i]
                    temp+=1
            return temp

        left,right=max(nums),sum(nums)
        total=0
        while left<=right:
            mid=(left+right)//2
            if part(mid)>k:
                left=mid+1
                
            else:
                right=mid-1
                total=mid
        return total



        