class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        window = set()


        left = 0
        for right in range(len(nums)):
            if nums[right] in window:
                return True

            window.add(nums[right])
        
            if len(window) > k:
                window.remove(nums[left])
                left += 1
            
            
        
        return False



            

        return False
                     
