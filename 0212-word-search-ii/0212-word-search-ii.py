class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # prefixes = set()

        # for word in words:
        #     for i in range(1,len(word)+1):
        #         pre = word[:i]
        #         prefixes.add(pre)

        # word_sets = set(words)
        
        root = TrieNode()

        for word in words:
            node = root

            for char in word:

                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word
        
        result = []

     
        def dfs(r,c,node):

            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return

            

            if board[r][c] == "#":
                return
            
            # current += board[r][c]

            # if current not in prefixes:
            #     return 

            # if current in word_sets:
            #     result.add(current)
                
            char = board[r][c]

            if char not in node.children:
                return

            node = node.children[char]

            if node.word:
                result.append(node.word)
                node.word = None

            
            board[r][c] = "#"

            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c-1,node)
            dfs(r,c+1,node)

            # dfs(r+1,c,current)
            # dfs(r-1,c,current)
            # dfs(r,c-1,current)
            # dfs(r,c+1,current)


            board[r][c] = char
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                # dfs(r,c,"")
                dfs(r,c,root)

        return result

        # return list(result)

