class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        arr = [i for i in range(1,n+1)]

        def circulaArr(a,b,i=0):
            if a == 1:
                return arr[0]
            
            i = (i + b - 1) % a
            arr.pop(i)
            a -= 1

            return circulaArr(a,b,i)
        
        return circulaArr(n,k)




