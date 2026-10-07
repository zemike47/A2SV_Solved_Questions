from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh = 0

        # Put ALL rotten oranges into the queue.
        # Count all fresh oranges.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q and fresh > 0:

            # Process exactly one BFS level = one minute
            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check boundaries
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Only fresh oranges can become rotten
                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1

                    q.append((nr, nc))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes