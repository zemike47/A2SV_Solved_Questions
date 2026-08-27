class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        three_three = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                R, C = r // 3, c // 3
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in three_three[(R,C)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                three_three[(R,C)].add(board[r][c])
        
        return True



            



