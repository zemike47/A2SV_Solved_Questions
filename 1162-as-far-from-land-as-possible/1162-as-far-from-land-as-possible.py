class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        from collections import deque
        queue = deque()
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    queue.append((r,c))
                else:
                    grid[r][c] = -1
        
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        max_distance = 0
        
        if len(queue) == n * n or len(queue) == 0:
            return -1
        
        while queue:

            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr , dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == -1:
                            grid[nr][nc] = grid[r][c] + 1
                            max_distance = max(max_distance,grid[nr][nc])
                            queue.append((nr,nc))
            
        return max_distance
            
