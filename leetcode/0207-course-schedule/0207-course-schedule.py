class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        

        queue = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neig in graph[node]:
                indegree[neig] -= 1

                if indegree[neig] == 0:
                    queue.append(neig)

        
        return len(order) == numCourses
                    


