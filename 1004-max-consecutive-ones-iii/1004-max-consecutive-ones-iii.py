class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt_binary = defaultdict(int)
        n = len(nums)
        left = 0
        max_len = float("-inf")
        

        for right in range(n):
            cnt_binary[nums[right]] += 1
            zeros_count = cnt_binary[0] 

            while cnt_binary[0]  > k:
                cnt_binary[nums[left]] -= 1
                if cnt_binary[nums[left]] == 0:
                    del cnt_binary[nums[left]] 

                left += 1
            
            max_len = max(max_len,right - left + 1)
        
        return max_len
            



            

        

        