class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        def sum(divisor):
            sum_=0
            for num in nums:
                sum_+=ceil(num/divisor)
            return sum_
        left,right,best_mid=1,nums[-1],0
        while left<=right:
            mid=(left+right)//2
            if sum(mid)>threshold:
                left=mid+1
            else:
                right=mid-1
                best_mid=mid
        return best_mid
        