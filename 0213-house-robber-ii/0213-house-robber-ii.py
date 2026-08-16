class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        def dynammicP(nums):
            prev1 = 0
            prev2 = 0

            for money in nums:
                curr = max(prev1,money + prev2)

                prev2 = prev1
                prev1 = curr
            
            return prev1

        

        case1 = dynammicP(nums[1:])
        case2 = dynammicP(nums[:n-1])

        return max(case1,case2)



        
