class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        cols = set()
        posDiagonals = set()
        negDiagonals = set()

        result = []


        def backtrack(r):
            
            if r == n:
                ans  = ["".join(row) for row in board]
                result.append(ans)
                return

            for c in range(n):
                if c in cols or (r+c) in posDiagonals or (r-c) in negDiagonals:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                posDiagonals.add(r+c)
                negDiagonals.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                posDiagonals.remove(r+c)
                negDiagonals.remove(r-c)

        
        backtrack(0)

        return result

        








