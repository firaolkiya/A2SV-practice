class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=[-1]*(len(nums)+1)
        for n in nums:
            ans[n]=n
        for i in range(len(ans)):
            if ans[i]==-1:
                return i
