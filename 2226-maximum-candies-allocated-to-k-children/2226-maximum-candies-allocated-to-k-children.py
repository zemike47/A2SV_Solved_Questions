class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left = 1
        right = max(candies)

        def allocate(x):

            total = 0
            for candy in candies:
                curr = candy // x

                total += curr
            
            return total >= k

        
        ans = 0
        while left <= right:
            mid = (left + right) // 2

            if allocate(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
