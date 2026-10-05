class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for num in range(1,amount+1):

                if coin <= num:
                    dp[num] += dp[num - coin]
        
        return dp[amount]

    