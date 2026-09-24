class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            count = 1

            for dr , dc in directions:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[i][j]:
                    count = max(count, 1 + dfs(nr,nc))
            
            dp[(i,j)] = count
            return count
                


        result = 1
        for i in range(m):
            for j in range(n):
                length = dfs(i,j)

                result = max(result,length)
        
        return result
        


        
        





