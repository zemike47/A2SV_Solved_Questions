class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums 

        # n = len(nums)
        # ans = [0] * (2 * n)
        # for i in range(n):
        #     ans[i] = ans[i+n] = nums[i]
        
        # return ans

        