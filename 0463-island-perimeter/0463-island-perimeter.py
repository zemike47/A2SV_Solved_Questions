class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c):
            nonlocal perimeter

            for dr,dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    dfs(nr,nc)

                elif nr < 0 or nr >= len(grid):
                    perimeter += 1
                
                elif nc < 0 or nc >= len(grid[0]):
                    perimeter += 1
                
                elif grid[nr][nc] == 0:
                    perimeter += 1


                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 2

                    dfs(r,c)

                    return perimeter

