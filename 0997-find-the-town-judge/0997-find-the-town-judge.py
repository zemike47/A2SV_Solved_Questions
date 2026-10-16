class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        graph = [[] for _ in range(n+1)]

        for u , v in trust:
            graph[u].append(v)
        
        ans = -1
        count = 0 

        for i in range(1,n+1):
            if len(graph[i]) == 0:
                count += 1
                ans = i
        
        if count > 1:
            return -1
        
        for i in range(1,n+1):
            if ans != i and ans not in graph[i]:
                return -1
        
        return ans
        