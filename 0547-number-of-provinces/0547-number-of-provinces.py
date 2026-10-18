class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] > self.size[root_y]:
            root_x , root_y = root_y,root_x
        
        self.size[root_x] += self.size[root_y]
        self.size[root_y] = 0

        self.parent[root_y] = root_x

        self.components -= 1

        return True



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        dsu = DSU(len(isConnected))

        for r in range(len(isConnected)):
            for c in range(r+1,len(isConnected)):
                if isConnected[r][c] == 1:

                    dsu.union(r,c)

        
        return dsu.components
                        
