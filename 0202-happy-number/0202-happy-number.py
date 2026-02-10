class Solution:
    def isHappy(self, n: int) -> bool:

        def check(n):
            new_num = 0
            while n > 0:
                r = n % 10
                new_num += r ** 2
                n //= 10
            return new_num

        s = set()
        s.add(n)

        while n != 1:
            n = check(n)
            if n in s:
                return False
            s.add(n)

        return True
