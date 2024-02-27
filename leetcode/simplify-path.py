class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        file_content=path.split("/")
        for p in file_content:
            if p==".." :
                if stack:
                    stack.pop()
            elif p!="." and p!="":
                stack.append(p)
        return "/"+"/".join(stack)
                
