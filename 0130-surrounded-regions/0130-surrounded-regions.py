class Solution:
    def solve(self, board):
        if not board:
            return
        
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(r, c):
            stack = [(r, c)]
            region = []
            is_surrounded = True
            
            while stack:
                x, y = stack.pop()
                
                if visited[x][y]:
                    continue
                
                visited[x][y] = True
                region.append((x, y))
                
                # If touches border → not surrounded
                if x == 0 or y == 0 or x == m-1 or y == n-1:
                    is_surrounded = False
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == 'O' and not visited[nx][ny]:
                            stack.append((nx, ny))
            
            return region, is_surrounded
        
        # Traverse entire board
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    region, is_surrounded = dfs(i, j)
                    
                    if is_surrounded:
                        for x, y in region:
                            board[x][y] = 'X'