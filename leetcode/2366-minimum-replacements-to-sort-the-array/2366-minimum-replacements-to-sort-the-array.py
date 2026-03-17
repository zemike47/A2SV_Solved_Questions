class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        limit = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            if nums[i] > limit:
                k = (nums[i] + limit - 1) // limit
                ops += k -1
                limit = nums[i] // k
            else:
                limit = nums[i]

        return ops


            
        

            
