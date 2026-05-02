class Solution:
    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        # visited = [[False] * cols for _ in range(rows)]

        def dfs(i,j):
            if i < 0 or i == rows  or j < 0 or j == cols or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1

        return count


        
        
