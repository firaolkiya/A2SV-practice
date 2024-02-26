class RecentCounter:

    def __init__(self):
        self.stack=[]
        self.recent_limit=0

    def ping(self, t: int) -> int:
        self.stack.append(t)
        while t-self.stack[self.recent_limit]>3000:
            self.recent_limit+=1
        return len(self.stack)-self.recent_limit
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)