class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]

        for course,pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        q = deque()

        for course in range(numCourses):
            if incoming[course] == 0:
                q.append(course)

        order = []
        # q = deque()

        while q:
            n = q.popleft()
            order.append(n)

            for nei in graph[n]:
                incoming[nei] -= 1

                if incoming[nei] == 0:
                    q.append(nei)
                    

        if len(order) != numCourses:
            return []
        
        return order

