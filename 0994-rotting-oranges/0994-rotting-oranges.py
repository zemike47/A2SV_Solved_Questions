class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        from collections import deque
        INF = 2147483647

        queue = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        minute = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue and fresh > 0:
            
            for _ in range(len(queue)):
                r,c = queue.popleft()


                for dr ,dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr,nc))
                            fresh -= 1
                
            minute += 1
        
        
        return  minute if fresh == 0 else -1 

