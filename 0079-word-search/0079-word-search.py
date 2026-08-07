class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #prunning one
        word_count = collections.Counter(word)

        board_count = collections.Counter([ch for row in board for ch in row])

        for ch in word:
            if word_count[ch] > board_count[ch]:
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]


        def dfs(r,c,index):

            if index == len(word):
                return True


            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False
        
            
            if board[r][c] != word[index]:
                return False
            
            
            temp = board[r][c]
            board[r][c] = "#"

            found = (dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1))
            board[r][c] = temp

            return found 

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True

        return False