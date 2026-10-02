class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
      
        left =0 
        count_zeros = 0

        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1
            
            
            while count_zeros > 0:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
                
            
            ans = max(ans,right - left + 1)
        
        return ans 
    
