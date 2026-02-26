class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        n = len(nums)
        ans = 0
        left = 0
        binary_map = defaultdict(int)

        for right in range(n):
            binary_map[nums[right]] += 1

            while binary_map[0] > 1:
                binary_map[nums[left]] -= 1
                left += 1
            
            ans = max(ans,right - left)
        
        return ans
                


