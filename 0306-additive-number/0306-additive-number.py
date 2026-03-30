class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)

        def string_add(num1,num2):
            i , j = len(num1) - 1, len(num2) - 1
            res = []
            carry = 0

            while i >= 0 or j >= 0 or carry:
                
                n1 = int(num1[i]) if i >= 0 else 0
                n2 = int(num2[j]) if j >= 0 else 0


                total = n1 + n2 + carry

                carry = total // 10

                res.append(str(total % 10))

                i -= 1
                j -= 1
            
            return "".join(reversed(res))

       
        def backtrack(start,curr):
            if start == n and len(curr) >= 3:
                return True
            

            for end in range(start+1,n+1):
                number = num[start:end]

                if len(number) > 1 and number.startswith("0"):
                    break

                
                if len(curr) >= 2:
                    expected = string_add(curr[-2],curr[-1])
                    if number != expected:
                        continue

                curr.append(number)

                if backtrack(end,curr):
                    return True
                    
                curr.pop()

            return False

        return backtrack(0,[])
        








    


                    


