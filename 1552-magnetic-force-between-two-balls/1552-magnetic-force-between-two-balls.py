class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(dist):
            count = 1
            last = position[0]

            for pos in position[1:]:
                if pos - last >= dist:
                    count += 1
                    last = pos

                if count >= m:
                    return True

            return False

        left = 1
        right = position[-1] - position[0]

        ans = 1

        while left <= right:
            mid = (left + right) // 2

            if can_place(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans