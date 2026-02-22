class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):

            n = target - nums[i]

            if nums[i] in seen:
                return [seen[nums[i]], i]

            seen[n] = i
        
            