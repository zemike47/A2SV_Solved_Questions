class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            left = 0
            window = 0
            ans = 0

            for right in range(len(nums)):
                window += nums[right]

                while window > goal:
                    
                    window -= nums[left]
                    left += 1
                  
                ans += right-left+1
                
            return ans 

        if goal > 0:
            return atMost(goal) - atMost(goal-1)
        else:
            return atMost(goal)

         

                
                

                


