class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = {}

        for source , destination in tickets:
            if source in graph:
                graph[source].append(destination)

            else:
                graph[source] = [destination]

        
        for source in graph:
            graph[source].sort(reverse=True)

        print(graph)

        
        stack = ["JFK"]

        path = []

        
        def dfs(node):

            while graph.get(node):

                next_dst = graph[node].pop()
                dfs(next_dst)
                    
            path.append(node)

        dfs("JFK")

        return path[::-1]
                

        


