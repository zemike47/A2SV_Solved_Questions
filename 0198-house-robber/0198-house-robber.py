class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)


        prev2 = 0
        prev1 = nums[0]
        
        for i in range(2,n+1):
            skip = prev1
            take = nums[i-1] + prev2

            current = max(take,skip)

            prev2 = prev1
            prev1 = current
        
        
        return prev1


