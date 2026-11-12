class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        if  len(word) > m*n:
            return False

        visited = [[False] * n for _ in range(m)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        def dfs(r,c,i):

            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True
        

            visited[r][c] = True

            for dr , dc in directions:
                nr,nc = dr + r , dc + c

                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    continue

                if dfs(nr,nc,i+1):
                    return True
                
            visited[r][c] = False   
            return False


        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        
        return False
                




        
