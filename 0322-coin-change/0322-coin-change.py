class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for num in range(1,amount+1):

                if coin <= num:
                    dp[num] = min(dp[num], 1 + dp[num - coin])
        
        return dp[amount] if dp[amount] != float("inf") else -1

    