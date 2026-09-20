class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev1, prev2 = 0, 0

        for i in range(n):
            current = min(cost[i] + prev1, cost[i] + prev2)

            prev2 = prev1
            prev1 = current

        return min(prev1, prev2)