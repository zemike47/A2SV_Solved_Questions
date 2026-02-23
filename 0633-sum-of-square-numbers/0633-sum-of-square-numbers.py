class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        

        limit = int(math.isqrt(c))

        left , right = 0 , limit

        while left <= right:
            curr_sum  = left ** 2 + right ** 2

            if curr_sum == c:
                return True
            elif curr_sum > c:
                right -= 1
            else:
                left += 1
        
        return False




