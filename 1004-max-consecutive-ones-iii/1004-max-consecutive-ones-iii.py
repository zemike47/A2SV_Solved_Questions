class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left =0 
        count_ones = 0
        count_zeros = 0

        ans = float("-inf")

        for right in range(len(nums)):
            if nums[right] == 1:
                count_ones += 1
            else:
                count_zeros += 1
            
            
            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                    left += 1
                else:
                    count_ones -= 1
                    left += 1
            
            ans = max(ans,right - left + 1)
        
        return ans 