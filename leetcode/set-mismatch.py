class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        store=[0]*len(nums)
        for num in nums:
            store[num-1]+=1
        ans=[0,0]
        for i in range(len(nums)):
            if store[i]==2:
                ans[0]=(i+1)
            elif store[i]==0:
                ans[1]=i+1
        return ans
