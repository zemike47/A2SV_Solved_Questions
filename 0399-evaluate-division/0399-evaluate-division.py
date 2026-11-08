class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for (node1,node2),weight in zip(equations,values):
            graph[node1].append((node2,weight))
            graph[node2].append((node1,1 / weight))

        
        def dfs(node1,node2,product,visited):
            
            visited.add(node1)
            for negh , weight in graph[node1]:
                if negh in visited:
                    continue
                
                if negh == node2:
                    return product * weight
                
                result = dfs(negh,node2,product * weight,visited)

                if result != -1.0:
                    return result
            
            return -1.0

        
        result = []
        print(graph)
        for n1,n2 in queries:

            if n1 not in graph or n2 not in graph:
                result.append(-1.0)
                continue

            if n1 == n2:
                result.append(1.0)
                continue


            ans = dfs(n1,n2,1.0,set())

            result.append(ans)
        
        return result






