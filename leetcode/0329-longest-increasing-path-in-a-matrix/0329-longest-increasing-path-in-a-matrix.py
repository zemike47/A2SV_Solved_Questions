class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n) for _ in range(m)]

        def dfs(r,c):

            if dp[r][c] != 0:
                return dp[r][c]

            dp[r][c] = 1

            directions = [(0,1),(1,0),(-1,0),(0,-1)]

            for dr,dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c],1 + dfs(nr,nc))

            
            return dp[r][c]





        ans = 0

        for r in range(m):
            for c in range(n):

                ans = max(ans, dfs(r,c))

        return ans

                