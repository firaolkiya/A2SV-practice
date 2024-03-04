class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        provedList=[]

        def prove(temp_list,sum_,k):
            if sum_>target:
                return
            for index in range(len(candidates)):
                sum_+=candidates[index]
                temp_list.append(candidates[index])
                proving =[num for num in sorted(temp_list)]
                if sum_==target and proving not in provedList:
                    provedList.append(proving[:])
                prove(temp_list,sum_,index+1)
                sum_-=temp_list.pop()
        prove([],0,0)
        
        return provedList