class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = []

        # for i in range(1,n+1):
        #     if nums[i-1] == -1:
        #         # if i+1 not in ans:
        #         ans.append(i)
        #     else:
        #         nums[i-1] = -1
        
        # print(ans)

        ans = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num)) 
            else:
                nums[abs(num)-1] *= -1

        return ans