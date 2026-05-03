class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        ans = []
        path = []
        path.append(0)

        def dfs(node):
            
            for nei in graph[node]:

                if nei == n - 1:
                    path.append(nei)
                    ans.append(path[:])
                    path.pop()
                    
                else:
                    path.append(nei)
                    dfs(nei)
                    path.pop()

        dfs(0)
        return ans




