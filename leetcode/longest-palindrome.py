class Solution:
    def longestPalindrome(self, s: str) -> int:
        m=Counter(s)
        cn=0
        for el in m:
            if m[el]%2!=0:
                cn+=1
        if cn==0 or cn==1:
            return len(s)
        return len(s)-cn+1

        