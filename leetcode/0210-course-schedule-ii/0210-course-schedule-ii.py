class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course , prerequiestie in prerequisites:
            graph[prerequiestie].append(course)
            indegree[course] += 1
        

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


        if len(order) != numCourses:
            return []
        
        return order             