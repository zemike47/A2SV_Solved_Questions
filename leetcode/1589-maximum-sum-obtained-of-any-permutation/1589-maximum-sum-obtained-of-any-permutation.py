class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = pow(10,9) + 7
        n = len(nums)

        freq = [0] * (n+1)

        for l ,r in requests:
            freq[l] += 1

            if r + 1 < n+1:
                freq[r+1] -= 1

        
        for i in range(1,n):
            freq[i] += freq[i-1]

        
        freq = freq[:n]

        nums.sort()
        freq.sort()

        res = 0
        for i in range(len(nums)):
            res = (res + nums[i] * freq[i]) % mod

        return res


