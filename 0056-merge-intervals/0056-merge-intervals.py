class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        newintervals = sorted(intervals, key=lambda x: x[0])

        left = 0

        while left < len(newintervals):
            a = [newintervals[left][0], newintervals[left][1]]
            right = left + 1   

            while right < len(newintervals) and a[1] >= newintervals[right][0]:
                a[1] = max(a[1], newintervals[right][1])
                right += 1

            ans.append(a)
            left = right  

        return ans
