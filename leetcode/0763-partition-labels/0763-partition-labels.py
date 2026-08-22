class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        lastIndexChar = {}

        for i , c in enumerate(s):
            lastIndexChar[c] = i

        start = end = 0
        size = 0
        res = []
        
        for i , c in enumerate(s):
            size += 1


            end = max(end,lastIndexChar[c])

            if i == end:
                res.append(size)
                size = 0
            
        return res


        
