class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        
        n = len(rooms)
        visited = [False] * n
        visited[0] = True

        queue = deque([0])


        while queue:

            for _ in range(len(queue)):
                i = queue.popleft()

                for room in rooms[i]:
                    if visited[room]:
                        continue
                    queue.append(room)
                    visited[room] = True
        
        if False in visited:
            return False
        
        return True

