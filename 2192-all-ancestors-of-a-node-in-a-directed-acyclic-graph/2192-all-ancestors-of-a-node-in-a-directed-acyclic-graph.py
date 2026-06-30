class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
  
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        anc = [set() for _ in range(n)]

        q = deque(i for i in range(n) if indegree[i] == 0)

        while q:
            u = q.popleft()

            for v in graph[u]:
                anc[v].update(anc[u])   # ancestors of u
                anc[v].add(u)           # u itself

                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return [sorted(s) for s in anc]