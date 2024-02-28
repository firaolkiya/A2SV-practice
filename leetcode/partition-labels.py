class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter=Counter(s)
        answer=[]
        temp=set()
        start=0
        for index, char in enumerate(s):
            temp.add(char)
            counter[char]-=1
            finished=True
            for k in temp:
                if counter[k]!=0:
                    finished=False
            if finished:
                answer.append(index-start+1)
                start=index+1
                temp=set()
        return answer
                    

