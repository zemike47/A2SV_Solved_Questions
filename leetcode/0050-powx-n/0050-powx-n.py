class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurssionPow(a,b):

            if b == 0:
                return 1

            value = recurssionPow(a,b//2)

            if b % 2 == 0:
                return value * value
            else:
                return value * value * a

        if n < 0:
            return 1 / recurssionPow(x,abs(n))
        
        return recurssionPow(x,n)

 


        