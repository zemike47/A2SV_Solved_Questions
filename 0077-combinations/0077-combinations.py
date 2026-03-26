class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []

        def backtracking(start,comb):
            if len(comb) == k:
                ans.append(comb.copy())
                return 
            
            for i in range(start,n+1):
                comb.append(i)
                backtracking(i+1,comb)
                comb.pop()

        backtracking(1,[])

        return ans