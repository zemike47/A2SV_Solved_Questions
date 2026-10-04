class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [[False] * (target + 1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(1,n+1):
            num = nums[i-1]
            for s in range(target + 1):
                dp[i][s] = dp[i-1][s]

                if num <= s:
                    dp[i][s] = dp[i-1][s] or dp[i-1][s-num]
            
        return dp[n][target]