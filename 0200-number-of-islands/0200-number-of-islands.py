class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r,c):
            directions = [(-1,0),(0,1),(1,0),(0,-1)]

            visited[r][c] = True

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and  not visited[nr][nc] and grid[nr][nc] == '1':
                    dfs(nr,nc)

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r,c)
                    count += 1

        return count