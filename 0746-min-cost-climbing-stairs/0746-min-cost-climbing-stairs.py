class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        prev2 = 0
        prev1 = cost[0]

        for i in range(2, n + 1):
            current = min(cost[i-1] + prev2,cost[i-1] + prev1)

            prev2 = prev1
            prev1 = current
            

        return min(prev1,prev2)