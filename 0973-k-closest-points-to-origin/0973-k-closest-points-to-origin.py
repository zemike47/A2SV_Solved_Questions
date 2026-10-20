class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        import heapq

        heap = []

        for x, y in points:
            dist = x ** 2 + y ** 2

            heapq.heappush(heap,(-dist,[x,y]))

            if len(heap) > k:
                _, [x,y] = heapq.heappop(heap)


        
        result = []

        for _ , [x,y] in heap:
            result.append([x,y])
        
        return result


