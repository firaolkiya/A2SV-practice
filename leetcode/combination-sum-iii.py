class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        validated = []
    
        def createComb(start,sum_,temp_list):
            if start==10:
                return
            for num in range(start,10):
                sum_ +=num
                temp_list.append(num)
                if sum_==n and len(temp_list)==k:
                    validated.append(temp_list[:])
                createComb(num+1,sum_,temp_list)
                sum_ -=temp_list.pop()
        createComb(1,0,[])
        return validated
