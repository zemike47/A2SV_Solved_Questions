class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()

        def get_next(n):

            total = 0
            
            while n > 0:
                r = n % 10
                total += r ** 2
                n //= 10
            
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and fast != slow:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        
        return fast == 1
    