class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix= defaultdict(int)
        prefix[0] = 1

        count = 0
        window_sum = 0

        for num in nums:

            window_sum += num

            remaining = window_sum - k

            if remaining in prefix:
                count += prefix[remaining]
        
            prefix[window_sum] += 1
    
        return count
