class RecentCounter:

    def __init__(self):
        self.stack = []
        

    def ping(self, t: int) -> int:
        self.stack.append(t)
        count = 0
        r = t - 3000

        for calls in self.stack:
            if r <= calls <= t:
                count += 1
        
        return count
        

        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)