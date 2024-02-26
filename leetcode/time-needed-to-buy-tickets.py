class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        arrange=deque()
        for i in tickets:
            arrange.append(i)
        counter=0
        timer=0
        while True:
            current_person=arrange.popleft()
            if current_person>0:
                timer+=1
                current_person-=1
            arrange.append(current_person)
            if counter%len(tickets)==k and current_person==0:
                return timer
            counter+=1
        return timer