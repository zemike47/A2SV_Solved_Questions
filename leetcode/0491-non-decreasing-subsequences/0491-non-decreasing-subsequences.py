class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        set_ans = set()
        n = len(nums)
        
        def backtrack(idx,curr):
            if len(curr) >= 2:
                ans.append(curr.copy())
                # if curr not in set_ans:
                #     ans.append(curr.copy())
                #     set_ans.append(curr)
            
            if idx >= n:
                return
            
            used = set()  

            
            for i in range(idx,n):
                if nums[i] in used:
                    continue

        
                if len(curr) == 0 or nums[i] >= curr[-1]:
                    used.add(nums[i])
                    
                    curr.append(nums[i])
                

                    backtrack(i+1,curr)

                    curr.pop()


        backtrack(0,[])
        return ans