class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left,right,best=0,len(letters)-1,letters[0]
        while left<=right:
            mid=(right+left)//2
            if letters[mid]>target:
                best=letters[mid]
                right=mid-1

            else:
                left=mid+1
        return best
