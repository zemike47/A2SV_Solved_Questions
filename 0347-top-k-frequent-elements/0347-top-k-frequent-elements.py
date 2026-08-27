class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq


        heap = []

        count = Counter(nums)
        print(count)

        for num,freq in count.items():

            heapq.heappush(heap,(freq,num))
        

        while len(heap) != k:
            heapq.heappop(heap)
        
        ans = []

        for freq, num in heap:
            ans.append(num)
        
        return ans
            
        





            

            



   