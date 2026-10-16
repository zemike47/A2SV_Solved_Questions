class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        queue = deque([(sr,sc)])
        orginal = image[sr][sc]
        image[sr][sc] = color

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                    if image[nr][nc] != color:
                        if image[nr][nc] == orginal:
                            image[nr][nc] = color
                            queue.append((nr,nc))
        
        return image


