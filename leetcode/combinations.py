class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination=[]
        def comb(temp_list,num):
            
            if len(temp_list)==k:
                combination.append(temp_list.copy())
                return 
            for temp_num in range(num,n+1):
                temp_list.append(temp_num)
                comb(temp_list,temp_num+1)
                temp_list.pop()
        comb([],1)
        return combination