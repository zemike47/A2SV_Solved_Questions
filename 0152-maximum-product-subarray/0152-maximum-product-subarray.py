class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        curr_max = nums[0]
        curr_min = nums[0]
        result = curr_max

        for num in nums[1:]:
            
            new_max = max(num,curr_max * num , curr_min * num)
            new_min = min(num,curr_max * num , curr_min * num)
        

            curr_max = new_max
            curr_min = new_min

            result = max(curr_max,result)
        


        
        return result



