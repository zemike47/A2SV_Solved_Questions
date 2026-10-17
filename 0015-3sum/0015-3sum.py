class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1


            while left < right:
                
                if nums[left] + nums[right] == -nums[i]:
                    result.append([nums[left] , nums[right] , nums[i]])

                    left += 1
                    right -= 1

                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
                    
                    while right >= 0 and nums[right] == nums[right+1]:
                        right -= 1

                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    left += 1

        return result

