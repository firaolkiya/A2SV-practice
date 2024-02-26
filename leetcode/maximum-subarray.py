class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_number=0
        max_sum=float('-inf')
        running_sum=0
        for num in nums:
            running_sum+=num
            sum_=running_sum-min_number
            max_sum=max(sum_,max_sum)
            min_number=min(min_number,running_sum)
        return max_sum


