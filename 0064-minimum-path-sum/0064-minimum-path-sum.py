class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        result = float("inf")

        memo = {}

        def dfs(i,j):
            if i == m or j == n:
                return float("inf")
            
            if i == m- 1 and j == n - 1:
                return grid[i][j]

            if (i,j) in memo:
                return memo[(i,j)]

            
            right = dfs(i,j+1)
            down = dfs(i+1,j)

            memo[(i,j)] = grid[i][j] + min(down,right)

            return memo[(i,j)]

        
        return dfs(0,0)
