class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        overall=defaultdict(int)
        counter=defaultdict(int)
        for index,num in enumerate(nums):
            overall[num]+=index
            counter[num]+=1
        arr=[0]*len(nums)
        prev = defaultdict(int)
        prevCo=defaultdict(int)
        for i in range(len(nums)):
            arr[i]=(overall[nums[i]]-(i*counter[nums[i]]))+(i*prevCo[nums[i]]-prev[nums[i]])
            overall[nums[i]]-=i
            prev[nums[i]]+=i
            prevCo[nums[i]]+=1
            counter[nums[i]]-=1

        return arr