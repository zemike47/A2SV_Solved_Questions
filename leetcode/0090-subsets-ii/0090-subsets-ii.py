class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        n = len(nums)
        nums.sort()

        def backtrack(start,curr):

            ans.append(curr.copy())




            for i in range(start,n):
                if i > start and nums[i] == nums[i-1]:
                    continue
             
                curr.append(nums[i])

                backtrack(i+1,curr)


                curr.pop()


        backtrack(0,[])
        return ans
