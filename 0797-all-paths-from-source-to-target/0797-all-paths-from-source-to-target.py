class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []
        path = [0]

        target = len(graph) - 1

        def dfs(node):
            # Base case: reached destination
            if node == target:
                result.append(path[:])
                return

            # Explore all neighbors
            for neighbor in graph[node]:
                path.append(neighbor)

                dfs(neighbor)

                # Backtrack
                path.pop()

        dfs(0)

        return result




