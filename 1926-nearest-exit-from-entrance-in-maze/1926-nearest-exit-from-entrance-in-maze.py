class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        
        directions = [(-1,0),
        (0,-1), (0,1),
        (1,0)
        ]

        visited = [[False] * len(maze[0]) for _ in range(len(maze))]

        from collections import deque

        queue = deque()
        entrancerow, entrancecol = entrance
        queue.append((entrancerow, entrancecol))
        visited[entrancerow][entrancecol] = True
        length = 1

        while queue:

            for _ in range(len(queue)):
                r,c  = queue.popleft()

                for dr , dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                        if maze[nr][nc] == "." and not visited[nr][nc]:
                            if nr == 0 or nr == len(maze) - 1 or nc == 0 or nc == len(maze[0]) - 1:
                                    return length

                            queue.append((nr,nc))
                            visited[nr][nc] = True
                
            length += 1

        return -1

