class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

                if grid[r][c] == 1:
                    fresh += 1
                    
        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        if not fresh:
            return 0

        time = -1

        while queue:

            time += 1
            
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr ,dc in directions:
                    nr = dr + r
                    nc = dc + c
                

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if grid[nr][nc] == 1:
                        
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                
            

        if fresh:
            return -1
        
        return time

                    