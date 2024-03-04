class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permetuation = []
        def permit(temp_list):
            if len(temp_list)==len(nums):
                permetuation.append(temp_list[:])
                return 
            for i in range(len(nums)):
                if not nums[i] in temp_list:
                    temp_list.append(nums[i])
                    permit(temp_list)
                    temp_list.pop()
        permit([])
        return permetuation
