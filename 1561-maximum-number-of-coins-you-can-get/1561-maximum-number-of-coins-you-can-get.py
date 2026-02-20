class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        me = 0
        n = len(piles)

        for i in range(n//3,len(piles),2):
            me += piles[i]
        
        return me