class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != 0:
                continue
            
            temp1 = i
            temp2 = i +1

            while temp2 < len(nums):
                nums[temp1],nums[temp2] = nums[temp2],nums[temp1]
                temp1 += 1
                temp2 += 1
            
