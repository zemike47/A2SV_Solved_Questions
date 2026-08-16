class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 2:
            return min(cost[0],cost[1])

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(3,n+1):
            curr = cost[i-1] + min(prev1 , prev2)

            prev2 = prev1
            prev1 = curr

        return min(prev1,prev2)