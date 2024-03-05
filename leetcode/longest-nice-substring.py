class Solution:
    def isNice(self,s):
        for char in s:
            temp = char.upper() if char.islower() else char.lower()
            if not temp in s:
                return False
        return True
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        leng=len(s)
        for start in range(leng):
            for end in range(start+1,leng):
                if self.isNice(s[start:end+1]) and len(ans)<end-start+1 :
                    ans=s[start:end+1]
                


        return ans

            