class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        nums.sort()
        def subFind(temp_list,k):
            if k==len(nums):
                return 
            for index in range(k,len(nums)):
                temp_list.append(nums[index])
                if temp_list not in subset:
                    subset.append(temp_list[:])
                subFind(temp_list,index+1)
                temp_list.pop()
        subFind([],0)
        return subset