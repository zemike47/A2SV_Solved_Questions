class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # #dfs solution

        # rows = len(grid)
        # cols = len(grid[0])


        # def dfs(r,c):

        #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
        #         return 0

        #     grid[r][c] = 0

        #     size = 1
            
        #     size += dfs(r+1,c)
        #     size += dfs(r-1,c)
        #     size += dfs(r,c+1)
        #     size += dfs(r,c-1)

        #     return size
            

        # max_area = 0

        # for r in range(rows):
        #     for c in range(cols):

        #         if grid[r][c] == 1:
        #             area = dfs(r,c)

        #             max_area = max(max_area,area)

        
        # return max_area


        #bfs soluiton

        m = len(grid)
        n = len(grid[0])

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        max_area = 0

        for r in range(m):
            for c in range(n):

                if grid[r][c] == 0:
                    continue

                queue = deque([(r,c)])
                
                #mark it as visited
                grid[r][c] = 0

                area = 1

                while queue:

                    row , col = queue.popleft()

                    for dr,dc in directions:
                        nr = dr + row
                        nc = dc + col

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:

                            queue.append((nr,nc))
                            grid[nr][nc] = 0
                            area += 1
                    
                max_area = max(max_area,area)

        return max_area



        


