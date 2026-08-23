class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()

        while n != 1:

            if n in hash_set:
                return False

            hash_set.add(n)
            
           
            new_num = 0
            
            while n > 0:
                r = n % 10
                new_num += r ** 2
                n //= 10
            
            n = new_num

        
        return True
    