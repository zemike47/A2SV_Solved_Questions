class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])

        avarage_value = window / k

        for i in range(k,len(nums)):
            window += nums[i]

            window -= nums[i-k]

            curr_average = window / k

            avarage_value = max(avarage_value,curr_average)

        return avarage_value







