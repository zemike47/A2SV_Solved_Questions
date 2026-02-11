class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        

        nums.sort()

        left = 0
        right = left + 1

        max_len = float("-inf")

        

        while right < len(nums):
            if nums[right] == nums[right-1]:
                left += 1
                right += 1

            elif nums[right] - nums[right-1] == 1:
                right += 1
            else:
                left = right
                right += 1
            
            max_len = max(max_len,right - left )

        return max_len
            
        




        
        