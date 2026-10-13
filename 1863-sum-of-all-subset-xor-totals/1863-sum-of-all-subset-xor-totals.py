class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        
        total = 0
        def backtrack(start,path):
            nonlocal total
            result = 0

            for num in path:
                result ^= num
            
            total += result

            for i in range(start,len(nums)):

                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()



        backtrack(0,[])

        return total