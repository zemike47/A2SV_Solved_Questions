class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        tails = []

        from bisect import bisect_left
        
        for i in range(n):
            j = bisect_left(tails,nums[i])

            if j == len(tails):
                tails.append(nums[i])

            else:
                tails[j] = nums[i]

        return len(tails) 

            

