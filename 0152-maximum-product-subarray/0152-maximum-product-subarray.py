class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        curr_max = nums[0]
        curr_min = nums[0]
        answer = nums[0]


        for i in range(1,n):

            old_max = curr_max
            old_min = curr_min

            curr_max = max(old_max*nums[i],old_min*nums[i],nums[i])
            curr_min = min(old_min*nums[i],old_max*nums[i],nums[i])

            answer = max(answer,curr_max)

        return answer
