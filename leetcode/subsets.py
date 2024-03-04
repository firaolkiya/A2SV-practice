class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        def sub(temp_list,k):
            if k==len(nums):
                return
            for index in range(k,len(nums)):
                temp_list.append(nums[index])
                subset.append(temp_list[:])
                sub(temp_list,index+1)
                temp_list.pop()
        sub([],0)
        return subset
            



        