class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"

        n = len(num1)
        m = len(num2)

        num1,num2 = num1[::-1], num2[::-1]

        result = [0] * (m+n)

        for i in range(n):
            for j in range(m):
                product = int(num1[i]) * int(num2[j])

                result[i+j] += product 
                result[i+j+1] += result[i+j] // 10
                result[i+j]  %= 10



        result = result[::-1]
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        
        return "".join(map(str,result[i:]))





        


                


        