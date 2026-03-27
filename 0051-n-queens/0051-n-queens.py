class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        posDiagonal = set()
        negDiagonal = set()

        borad = [["."] * n for _ in range(n)]

        ans = []

        def backtrack(r):
            if r == n:
                res = ["".join(row) for row in borad]
                ans.append(res)
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

        return ans


