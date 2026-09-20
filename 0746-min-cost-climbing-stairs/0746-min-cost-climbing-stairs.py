class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # prev2 = 0
        # prev1 = cost[0]
        dp = [0] * (n+2)
        dp[n] = 0
       

        for i in range(n-1,-1,-1):
            dp[i] = min(cost[i] + dp[i+1] , cost[i] + dp[i+2])

            # prev2 = prev1
            # prev1 = current
        
        return min(dp[0],dp[1])