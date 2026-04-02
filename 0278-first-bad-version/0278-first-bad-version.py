# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # for i in range(1,n+1):
        #     ans = isBadVersion(i)

        #     if ans:
        #         print(i)
        #         return i

        left , high = 1 , n

        while left <= high:
            mid  = (left + high) // 2

            ans = isBadVersion(mid)

            if ans:
                high = mid - 1
            else:
                left = mid + 1
        
        return left


        