import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)

        # maintain the order 
        if self.right and -self.left[0] > self.right[0]:
            left = -heapq.heappop(self.left)
            right = heapq.heappop(self.right)

            heapq.heappush(self.left,-right)
            heapq.heappush(self.right,left)

        # balance heap left and right with 1
        if len(self.left) > len(self.right) + 1:
            num = -heapq.heappop(self.left)

            heapq.heappush(self.right,num)
        
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2

        return -self.left[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()