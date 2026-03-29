class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        set_ans = set()
        n = len(nums)
        
        def backtrack(idx,curr):
            if len(curr) >= 2:
                if curr not in ans:
                    ans.append(curr.copy())
                # if curr not in set_ans:
                #     ans.append(curr.copy())
                #     set_ans.append(curr)
            
            if idx >= n:
                return
            
            for i in range(idx,n):
                if len(curr) == 0 or nums[i] >= curr[-1]:
                    curr.append(nums[i])
                

                    backtrack(i+1,curr)

                    curr.pop()


        backtrack(0,[])
        return ans