class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        
        result = [intervals[0]]

        for start,end in intervals[1:]:

            if start <= result[-1][1]:
                s = min(start,result[-1][0])
                e = max(end,result[-1][1])

                result[-1] = [s,e]
            
            else:
                result.append([start,end])

        return result
