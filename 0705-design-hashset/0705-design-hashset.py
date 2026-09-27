class MyHashSet:

    def __init__(self):
        self.capacity = 100
        self.size = 100
        self.bucket = [[] for _ in range(self.capacity)]
    
    def getIndex(self,key:int) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        idx = self.getIndex(key)

        if key in self.bucket[idx]:
            return

        self.bucket[idx].append(key)
        self.size += 1
        

    def remove(self, key: int) -> None:
        idx = self.getIndex(key)

        if key not in self.bucket[idx]:
            return
        
        self.bucket[idx].remove(key)
        self.size -= 1
        

    def contains(self, key: int) -> bool:
        idx = self.getIndex(key)

        if key in self.bucket[idx]:
            return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)