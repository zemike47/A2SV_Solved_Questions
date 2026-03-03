class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixsum = 0
        prefixsum_map = defaultdict(int)
        prefixsum_map[0] = 1
        count = 0

        for i in range(len(nums)):
            prefixsum += nums[i]

            if (prefixsum - k) in prefixsum_map:
                count +=  prefixsum_map[prefixsum - k]
            
            prefixsum_map[prefixsum] += 1
        
        return count
            








