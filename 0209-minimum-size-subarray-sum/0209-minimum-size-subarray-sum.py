class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        left = 0
        window_sum = 0
        ans = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                ans = min(ans,right-left+1)
                window_sum -= nums[left]
                left += 1
            
    
        return ans if ans != float("inf") else 0


