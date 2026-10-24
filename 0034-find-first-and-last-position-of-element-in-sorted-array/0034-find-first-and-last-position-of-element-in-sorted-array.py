class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def findFirst(nums):
            left,right = 0 , len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left if left < len(nums) and nums[left] == target else -1
        
        def findLast(nums):
            left,right = 0 , len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return right if right >= 0 and nums[right] == target else -1
            

        result = []

        result.append(findFirst(nums))
        result.append(findLast(nums))

        return result


