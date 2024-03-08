class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        def search(value,index):
            left,right,best=0,len(nums)-1,0
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]+nums[index]>target:
                    right=mid-1
                else:
                    best=mid
                    left=mid+1
            return max(0,(best-index))
        ans=0
        mod=10**9 + 7
        for i in range(len(nums)):
            temp=search(nums[i],i)
            if temp==0:
                if nums[i]*2<=target:
                    ans+=1
                continue
            ans+=2**(temp)
        return ans%mod


                