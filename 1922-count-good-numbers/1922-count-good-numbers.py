class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = pow(10,9) + 7

        def countGood(a,b):
            if b == 0:
                return 1

            value = countGood(a,b//2)

            if b % 2 == 0:
                return (value * value) % mod
            else:
                return (value * value * a) % mod

        k = n // 2

        if n % 2 == 0:
            return (countGood(5,k) * countGood(4,k)) % mod
        else:
            return (countGood(5,k+1) * countGood(4,k)) % mod

        


        


            
            
