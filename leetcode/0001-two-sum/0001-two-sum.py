class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if hash_map and nums[i] in hash_map:
                return [i,hash_map[nums[i]]]
            
            hash_map[rem] = i
        
        







