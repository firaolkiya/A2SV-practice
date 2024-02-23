class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        updated=""
        leng=len(palindrome)
        if leng==1:
            return ""
        for i in range(leng):
            if palindrome[i]!="a" and not(leng%2!=0 and i==leng//2):
                updated=palindrome[:i]+"a"+palindrome[i+1:]
                return updated
        return palindrome[:leng-1]+"b"