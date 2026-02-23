class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = float("-inf")
        n = len(height)

        i , j = 0 , n - 1

        while i <= j:
            x = abs(j - i)
            y = min(height[j] , height[i])

            curr_amount_water = x * y

            max_amount = max(max_amount,curr_amount_water)

            if height[i] <= height[j]:
                 i += 1
            else:
                j -= 1
        
        return max_amount