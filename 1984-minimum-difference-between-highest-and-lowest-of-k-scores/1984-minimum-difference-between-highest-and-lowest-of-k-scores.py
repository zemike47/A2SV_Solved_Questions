class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        min_difference = float("inf")
        left = 0

        for right in range(len(nums) -k + 1):
            right = left + k -1 

            difference = nums[right] - nums[left]

            min_difference = min(min_difference,difference)

            left += 1

        return min_difference