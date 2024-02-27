class Solution:
    def play(self,nums,player):
        if len(nums)==1:
            scoreBoard=[0,0]
            scoreBoard[player%2]=nums[0]
            return scoreBoard
        left=self.play(nums[1:],player+1)
        right=self.play(nums[:-1],player+1)
        left[player%2]+=nums[0]
        right[player%2]+=nums[-1]
        if left[player%2]>right[player%2]:
            return left
        else:
            return right

    def predictTheWinner(self, nums: List[int]) -> bool:
        scoreBoard=self.play(nums,0)
        return scoreBoard[0]>=scoreBoard[1]