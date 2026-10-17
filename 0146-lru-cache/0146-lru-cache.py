class Node:
    def __init__(self,key,val,next=None,prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}

    def insert(self,node):

        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def remove(self,node):

        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key not  in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        if key in self.cache:

            node = self.cache[key]

            self.remove(node)

            node.val = value
            self.insert(node)

            return

        if len(self.cache) == self.capacity:
            lru = self.head.next

            self.remove(lru)

            del self.cache[lru.key]
        
        new_node = Node(key,value)
        self.insert(new_node)
        self.cache[key] = new_node


        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)