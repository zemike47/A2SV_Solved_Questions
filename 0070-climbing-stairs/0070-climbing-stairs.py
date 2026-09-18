class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 ,prev1 = 0,1

        for _ in range(1,n+1):
            current = prev1 + prev2 
            prev2 = prev1
            prev1 = current

        return prev1