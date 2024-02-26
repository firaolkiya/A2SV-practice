class Solution:
    def decodeString(self, s: str) -> str:
        if not "[" in s:
            return s
        built=""
        start_num=start_bracket=net_bracket=-1
        iterator=0
        cofficient=""
        Flag=True
        while iterator<len(s):
            if not Flag:
                if s[iterator]=="[":
                    net_bracket+=1
                if s[iterator]=="]":
                    net_bracket-=1
                if net_bracket==0:
                    built+=int(cofficient)*self.decodeString(s[start_bracket:iterator])
                    start_num=start_bracket=net_bracket=-1
                    cofficient=""
                    Flag=True
            elif s[iterator].isdigit() and start_num==-1:
                start_num=iterator
            elif s[iterator].isdigit():
                pass
            elif s[iterator]=="[":
                cofficient=s[start_num:iterator]
                net_bracket=1
                Flag=False
                start_bracket=iterator+1
            else:
                built+=s[iterator]
            iterator+=1
        return built
