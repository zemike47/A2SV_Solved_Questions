class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        suffix_prod = [1] * n

        curre_pre = 1

        for i in range(1,n):
            curre_pre *= nums[i-1]
            prefix_prod[i] = curre_pre

        curr_suffix = 1
        for i in range(n-1,-1,-1):
            suffix_prod[i] = curr_suffix
            curr_suffix *= nums[i]

        ans  = [1] * n

        for i in range(n):
            ans[i] = prefix_prod[i] * suffix_prod[i]
        
        return ans 

          
        
        print(prefix_prod)
        print(suffix_prod)








      
        


        