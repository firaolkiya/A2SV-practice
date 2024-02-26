class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total_penality=float('inf')
        time=0
        size=len(customers)
        comes=[0]*(size+1)
        not_comes=[0]*(size+1)
        for i in range(size):
            comes[i+1]=comes[i]+int(customers[i]=="Y")
            not_comes[i+1]=not_comes[i]+int(customers[i]=="N")
        comes.append(comes[-1])
        not_comes.append(not_comes[-1])
        for i in range(1,size+2):
            temp_penality=not_comes[i-1]+comes[size]-comes[i-1]
            if temp_penality<total_penality:
                time=i-1
                total_penality=temp_penality
        return time
