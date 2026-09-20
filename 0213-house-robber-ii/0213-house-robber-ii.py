class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
         

        def rob(houses):
            n = len(houses)


            if n == 1:
                return houses[0]
            

            prev2 = 0
            prev1 = houses[0]
            
            for i in range(2,n+1):
                skip = prev1
                take = houses[i-1] + prev2

                current = max(take,skip)

                prev2 = prev1
                prev1 = current
            
            
            return prev1
        
        case1 = rob(nums[1:])
        case2 = rob(nums[:-1])

        return max(case1,case2)


