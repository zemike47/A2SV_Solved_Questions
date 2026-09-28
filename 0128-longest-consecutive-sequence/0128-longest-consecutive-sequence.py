class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        mx_len = 1
        nums_set = set(nums)

        for num in nums_set:
            length = 1

            if num - 1 not in nums_set:
                while num + 1 in nums_set:
                    num = num + 1
                    length += 1
            
            mx_len  = max(mx_len,length)
        
        return mx_len