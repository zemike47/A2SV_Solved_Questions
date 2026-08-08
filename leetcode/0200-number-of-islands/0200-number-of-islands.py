class Solution:
    def numIslands(self, grid):


        # def dfs(r,c):
        #     if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == "0":
        #         return 

        #     grid[r][c] = "0"
            
        #     dfs(r+1,c)
        #     dfs(r-1,c)
        #     dfs(r,c+1)
        #     dfs(r,c-1)

        # count = 0

        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):

        #         if grid[r][c] == "1":
        #             dfs(r,c)
        #             count += 1

        # return count


        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        islands = 0


        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "0":
                    continue

                queue = deque([(r,c)])
                grid[r][c] = "0"

                islands += 1

                while queue:
                    
                    row,col = queue.popleft()

                    for dr,dc in directions:
                        nr = row + dr
                        nc = col + dc 

                        if 0 <= nr < rows and 0 <= nc < cols:

                            if grid[nr][nc] == "1":
                                queue.append((nr,nc))
                                grid[nr][nc] = "0"

        return islands
                            






        
        
