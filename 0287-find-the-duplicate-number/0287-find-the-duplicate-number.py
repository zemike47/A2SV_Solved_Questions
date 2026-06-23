class Solution:
    def findDuplicate(self, nums):
        # slow = nums[0]
        # fast = nums[0]

        # # Step 1: detect cycle
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        # # Step 2: find entrance
        # slow = nums[0]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow

        dupilicate = -1

        for num in nums:
            if nums[abs(num) - 1] < 0:
                dupilicate = abs(num)
            
            else:
                nums[abs(num)-1] *= -1
        
        return dupilicate

