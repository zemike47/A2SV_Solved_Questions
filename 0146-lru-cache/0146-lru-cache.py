class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self,node) -> None:

        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def remove(self,node):

        node.prev.next = node.next
        node.next.prev = node.prev



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value

        
    def put(self, key: int, value: int) -> None:


        if key not in self.cache:
            node = Node(key,value)

            if len(self.cache) == self.capacity:
                lru = self.head.next

                self.remove(lru)
                del self.cache[lru.key]

            self.cache[key] = node
            self.insert(node)

            return
        
        node = self.cache[key]

        self.remove(node)

        node.value = value
        self.insert(node)
        



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)