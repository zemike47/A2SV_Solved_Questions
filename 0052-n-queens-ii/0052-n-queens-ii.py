
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = set()
        posDiagonal = set()
        negDiagonal = set()

        borad = [["."] * n for _ in range(n)]

        count = 0

        def backtrack(r):
            if r == n:
                nonlocal count
                count += 1
                return

            for c in range(n):
                if c in cols or (r + c) in posDiagonal or (r - c) in negDiagonal:
                    continue
                    
                borad[r][c] = 'Q'
                cols.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)

                backtrack(r+1)

                cols.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                borad[r][c] = '.'


        backtrack(0)

        return count


