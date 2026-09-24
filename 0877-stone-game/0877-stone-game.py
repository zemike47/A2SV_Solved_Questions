class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        dp = {}

        def dfs(l,r):
            if l > r:
                return 0
            
            if (l,r) in dp:
                return dp[(l,r)]
            
            alice_turn  = (r - l + 1) % 2 == 0

            left = piles[l] if alice_turn else 0
            right = piles[r] if alice_turn else 0

            dp[(l,r)] = max(dfs(l + 1,r) + left,dfs(l,r-1) + right)

            return dp[(l,r)]
        
        total = sum(piles)
        alice_score = dfs(0,len(piles) - 1)

        return alice_score > alice_score - total // 2

        

        