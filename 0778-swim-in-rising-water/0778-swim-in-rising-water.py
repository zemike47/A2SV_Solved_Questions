class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0],0,0)]
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        visited= set()



        while pq:
            time,i,j = heapq.heappop(pq)


            if (i,j) in visited:
                continue

            visited.add((i,j))

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return time

            
            for dr , dc in direction:
                nr = dr + i
                nc = dc + j

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if (nr,nc) not in visited:

                        new_time = max(time,grid[nr][nc])
                        # visited.add((nr,nc))

                        heapq.heappush(pq,(new_time,nr,nc))

            
                        