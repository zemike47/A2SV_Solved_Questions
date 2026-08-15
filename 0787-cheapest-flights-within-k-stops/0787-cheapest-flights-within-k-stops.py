class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = {i:float('inf') for i in range(n)}


        dist[src] = 0

        for i in range(k+1):
            new_dist = dist.copy()
            change = False

            for u,v,cost in flights:

                if dist[u] != float("inf") and dist[u] + cost < new_dist[v]:
                    new_dist[v] = dist[u] + cost
                    change = True

            dist = new_dist

            if not change:
                break
        

        if dist[dst] == float("inf"):
            return -1
        
        return dist[dst]

