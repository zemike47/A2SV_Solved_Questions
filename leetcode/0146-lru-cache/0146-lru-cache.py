class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.order = []

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node) -> None:
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev



    def insert(self,node) -> None:
        prev = self.tail.prev

        node.prev = prev
        node.next = self.tail

        prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val



    def put(self, key: int, value: int) -> None:

        if key in self.cache:

            node = self.cache[key] 
            node.val = value

            self.remove(node)
            self.insert(node)

            return

        
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next

            self.remove(lru)

            del self.cache[lru.key]

        
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)