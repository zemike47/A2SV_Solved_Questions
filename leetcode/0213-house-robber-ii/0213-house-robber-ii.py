class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # n = len(nums)

        def robLinear(nums):
            n = len(nums)
            # nonlocal n
        

            if n == 1:
                return nums[0]
            
           

            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])

            for i in range(2, n):
                curr = max(prev1, nums[i] + prev2)
                prev2 = prev1
                prev1 = curr

            return prev1
        
        if len(nums) == 1:
            return nums[0]
        
        return max(robLinear(nums[:len(nums)-1]),robLinear(nums[1:]))