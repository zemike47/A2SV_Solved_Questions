class Solution:
    def fib(self, n: int) -> int:
        
        def fibonacciNum(num):
            
            if num == 0:
                return 0
            if num == 1: 
                return 1
                

            return fibonacciNum(num-1) + fibonacciNum(num-2)

        return fibonacciNum(n)