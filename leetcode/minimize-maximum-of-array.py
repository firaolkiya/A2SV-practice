class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_element=0
        total=0
        for index,num in enumerate(nums):
            average=ceil((total+num)/(index+1))
            max_element=max(max_element,average)
            total+=num
        return max_element
