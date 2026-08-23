class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_q = sorted(queries)

        result = {}
        heap = []
        i = 0

        for q in sorted_q:

            while i < len(intervals) and intervals[i][0] <= q:
                left , right = intervals[i]
                size = right - left + 1
                i += 1

                heapq.heappush(heap,(size,right))

            
            while heap  and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                result[q] = heap[0][0]
            else:
                result[q] = -1
            
        
        return [result[q] for q in queries]

            


