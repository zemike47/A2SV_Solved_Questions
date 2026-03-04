class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        current = 0
        max_val = float("-inf")

        for i in range(len(nums)):
            current += nums[i]
            max_val = max(max_val,current)

            if current < 0:
                current = 0
            
        return max_val
            




        
