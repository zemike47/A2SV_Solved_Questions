class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        
        m = len(isWater)
        n = len(isWater[0])

        from collections import deque

        queue = deque()

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    isWater[r][c] = 0
                    queue.append((r,c))
                else:
                    isWater[r][c] = -1
        
        directions = [(1,0),
        (0,1),(-1,0),
        (0,-1),
        ]



        while queue:

            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr , dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < m and 0 <= nc < n:
                        if isWater[nr][nc] == -1:
                            isWater[nr][nc] = isWater[r][c] + 1
                            queue.append((nr,nc))
                
        return isWater



        
