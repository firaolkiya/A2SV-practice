class Solution:
    def numberOfWays(self, s: str) -> int:
        answer=0
        zero_prefix=[0]*(len(s)+1)
        one_prefix=[0]*(len(s)+1)
        for i in range(len(s)):
            zero_prefix[i+1]+=zero_prefix[i]+int(s[i]=="0")
            one_prefix[i+1]+=one_prefix[i]+int(s[i]=="1")
        for i in range(len(s)):
            if s[i]=="1":
                answer+=zero_prefix[i]*(zero_prefix[len(s)]-zero_prefix[i])
            else:
                answer+=one_prefix[i]*(one_prefix[len(s)]-one_prefix[i])
        return answer

        
