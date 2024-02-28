class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumb_step=nums[0]
        for i in range(1,len(nums)):
            if jumb_step==0:
                return False
            jumb_step=max(jumb_step-1,nums[i])
        return True

        