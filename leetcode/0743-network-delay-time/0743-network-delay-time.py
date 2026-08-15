class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist = {i:float("inf") for i in range(1,n+1)}
        dist[k] = 0

        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((t,v))

        import heapq

        pq = [(0,k)]

        while pq:

            curr_time , u = heapq.heappop(pq)

            if curr_time > dist[u]:
                continue

            for t,v in graph[u]:
                new_time = curr_time + t

                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(pq,(new_time,v))
        
        result = max(dist.values())

        return result if result != float("inf") else -1






