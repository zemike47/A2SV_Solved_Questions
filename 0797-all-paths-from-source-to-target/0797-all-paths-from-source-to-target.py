class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []


        def dfs(i,path):
    
            for negh in graph[i]:
                if negh == len(graph) - 1:
                    path.append(negh)
                    result.append(path.copy())
                    path.pop()
                else:
                    path.append(negh)
                    dfs(negh,path)
                    path.pop()
        
        dfs(0,[0])

        return result




