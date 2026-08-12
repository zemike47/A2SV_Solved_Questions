class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        import heapq

        graph = [[] for _ in range(n+1)]

        for u,v,w in times:
            graph[u].append((v,w))

        TIME = {node:float("inf") for node in range(1,n+1)}
        TIME[k] =  0

        min_heap = [(0,k)]

        while min_heap:
            t, node = heapq.heappop(min_heap)

            if t > TIME[node]:
                continue
            
            for neig,neig_t in graph[node]:
                curr_time = t + neig_t

                if curr_time < TIME[neig]:
                    TIME[neig] = curr_time
                    heapq.heappush(min_heap,(curr_time,neig))
                    

        
        if float("inf") in TIME.values():
            return -1
        
        return max(TIME.values())
        






        