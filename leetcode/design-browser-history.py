class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser=[homepage]
        self.current_position=0
        
    def visit(self, url: str) -> None:
        while len(self.browser)>self.current_position+1:
            self.browser.pop()
        self.browser.append(url)
        self.current_position+=1

    def back(self, steps: int) -> str:
        self.current_position-=min(self.current_position,steps)
        return self.browser[self.current_position]

    def forward(self, steps: int) -> str:
        self.current_position=min(len(self.browser)-1,self.current_position+steps)
        return self.browser[self.current_position]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)