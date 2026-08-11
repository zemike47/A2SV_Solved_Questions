class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        parent = list(range(n+1))
        size = [1] * (n+1)

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]

        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return [a,b]
            
            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            parent[rootB] = rootA
            size[rootA] += size[rootB]

        for a,b in edges:

            ans =  union(a,b)

            if ans:
                return ans 

