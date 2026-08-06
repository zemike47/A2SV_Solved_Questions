class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(start,curr_sum,path):
            if curr_sum == target:
                result.append(path.copy())

            if curr_sum > target:
                return


            for i in range(start,len(candidates)):
                path.append(candidates[i]) 
                curr_sum += candidates[i]

                backtrack(i,curr_sum,path)

                curr_sum -= candidates[i]
                path.pop()

        backtrack(0,0,[])

        return result
