class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        left = 1
        right = max(candies)

        ans = 0

        while left <= right:
            mid = (left + right) // 2

            children = 0

            for c in candies:
                children += c // mid

            if children >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans