class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times=times
        self.winnersBoard =[]
        scoreBoard=defaultdict(int)
        winner=persons[0]
        for i in range(len(times)):
            scoreBoard[persons[i]]+=1
            if scoreBoard[persons[i]]>=scoreBoard[winner]:
                winner=persons[i]
            self.winnersBoard.append(winner)
        print(self.winnersBoard)

    def q(self, t: int) -> int:
        index= (bisect_right(self.times,t))-1
        return self.winnersBoard[index]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)