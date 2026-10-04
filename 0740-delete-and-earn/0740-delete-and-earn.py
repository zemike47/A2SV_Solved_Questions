class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        c = Counter(nums)

        points = {}

        for k ,v in c.items():
            points[k] = k * v

        nums_set = sorted(set(nums))
        max_num = max(nums)

        dp = [0] * (max_num + 1)
        dp[1] = points.get(1,0) 

        
        for num in range(2,max_num+1):
            take = points.get(num,0)  + dp[num-2]
            skip = dp[num-1]

            dp[num] = max(take, skip)
        
        return dp[max_num]




            