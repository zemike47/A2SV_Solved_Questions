class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        ops = 0

        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            
            ops += 1
        
        if target > 1:
            ops += target - 1

        return ops



        