class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:       
       
        provedList=[]
        candidates.sort()
        def prove(temp_list,sum_,k):
            if k==len(candidates) or sum_>target:
                return
            for index in range(k,len(candidates)):
                if index>k and candidates[index-1]==candidates[index]:
                    continue
                sum_+=candidates[index]
                temp_list.append(candidates[index])
                if sum_==target:
                    provedList.append(temp_list[:])
                prove(temp_list,sum_,index+1)
                sum_-=temp_list.pop()
        prove([],0,0)
        
        return provedList