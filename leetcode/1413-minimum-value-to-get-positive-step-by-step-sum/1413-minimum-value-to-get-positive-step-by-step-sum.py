class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = []
        accumulator = 0

        for i in range(len(nums)):
            accumulator += nums[i]
            prefix.append(accumulator)
        
        min_m = min(prefix)

        if min_m < 0:
            return 1 - min_m
        
        else:
            return 1
    
        


            