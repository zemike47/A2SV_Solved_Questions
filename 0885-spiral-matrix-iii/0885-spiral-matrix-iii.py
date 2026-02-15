class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        result = []
        
        total = rows * cols
        r = rStart
        c = cStart
        result.append([r,c])

        dir = [(0,1),(1,0),(0,-1),(-1,0)]

        step = 1
        d = 0

        while len(result) < total:
            for _ in range(2):
                dr , dc = dir[d % 4]
                for _ in range(step):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r,c])
                
                d += 1
            step += 1
            


        return result
