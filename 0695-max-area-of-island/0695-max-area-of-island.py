class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
     
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] == 0:
                return 0
            
            visited[r][c] = True

            count = 1

            count += dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)

            return count


            
        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and not visited[r][c]:
                    count = dfs(r,c)
                    
                    max_area = max(max_area,count)

        return max_area