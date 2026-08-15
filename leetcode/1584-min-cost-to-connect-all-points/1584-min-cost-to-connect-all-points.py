class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        visited = set()

        i,j = points[0]
        # visited.add((i,j))

        pq = [(0,i,j)]

        cost = 0

        while len(visited) < n:
            dist , x1,y1 = heapq.heappop(pq)

            if (x1,y1) in visited:
                continue
            
            visited.add((x1,y1))
            cost += dist
            

            for x2 ,y2 in points:

                if (x2,y2) in visited:
                    continue
                
                distance = abs(x2-x1) + abs(y2-y1)

                heapq.heappush(pq,(distance,x2,y2))

        return cost
                






