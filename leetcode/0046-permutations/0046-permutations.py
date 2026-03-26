
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        comb_set = set()

        def backtracking(comb):
            if len(comb) == len(nums):
                ans.append(comb.copy())
                return 
            
            for i in range(len(nums)):
                if comb and nums[i] in comb_set:
                    continue

                comb.append(nums[i])
                comb_set.add(nums[i])

                backtracking(comb)

                comb.pop()
                comb_set.remove(nums[i])


        backtracking([])

        return ans