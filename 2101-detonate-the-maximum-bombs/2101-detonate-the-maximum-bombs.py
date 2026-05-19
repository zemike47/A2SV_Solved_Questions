class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        graph = collections.defaultdict(list)

        for i in range(n):

            x1,y1,r1 = bombs[i]

            for j in range(n):

                if i == j:
                    continue

                x2,y2, _ = bombs[j]

                d1 = x1 - x2
                d2 = y1 - y2

                if d1 * d1 + d2 * d2 <= r1 * r1:
                    graph[i].append(j)

        
        def dfs(i,visted):
            visted.add(i)

            for nei in graph[i]:
                if nei not in visted:
                    dfs(nei,visted)
            
        ans = 0

        for i in range(n):
            visited = set()

            dfs(i,visited)

            ans = max(ans,len(visited))

        return ans



                
            

