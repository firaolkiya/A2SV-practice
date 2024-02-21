class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits=Counter(answers)
        total=0
        print(ceil(3/10))
        for rabbit in rabbits:
            total+=ceil(rabbits[rabbit]/(rabbit+1))*(rabbit+1)
        return total