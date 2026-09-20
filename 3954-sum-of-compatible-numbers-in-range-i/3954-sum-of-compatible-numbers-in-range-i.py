class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        
        total = 0 
      
        end = k + n + 1

        for x in range(max(1,n-k),end):
            if n & x == 0:
                total += x
        
        return total