class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()

        for num in range(left,right+1):
            for i,j in ranges:
                if num >= i and num <= j:
                    break
            else:
                return False
        else:
            return True 

                

        