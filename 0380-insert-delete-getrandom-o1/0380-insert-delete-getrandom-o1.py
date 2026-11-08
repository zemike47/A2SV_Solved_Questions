class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False

        idx = len(self.nums)
        self.cache[val] = idx

        self.nums.append(val)


        return True

        
    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False

        idx = self.cache[val]
        last_idx = len(self.nums) - 1

        self.nums[idx], self.nums[last_idx] = self.nums[last_idx] ,self.nums[idx]

        
        
        self.cache[self.nums[idx]] = idx
        self.nums.pop()
        del self.cache[val]

        return True


    def getRandom(self) -> int:
        import random
        val = random.choice(self.nums)
        return val
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()