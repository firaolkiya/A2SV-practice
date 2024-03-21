class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp=[0]*len(nums)
        ans=[]
        for num in nums:
            temp[num-1]=num
        for i in range(len(temp)):
            if temp[i]==0:
                ans.append(i+1)
        return ans
                