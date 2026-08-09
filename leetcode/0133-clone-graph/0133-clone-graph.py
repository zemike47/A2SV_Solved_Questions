"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # if not node:
        #     return None
        
        # clones = {}

        # def dfs(node):

        #     if node in clones:
        #         return clones[node]

        #     clone = Node(node.val)
        #     clones[node] = clone

        #     for neighbor in node.neighbors:
        #         clone.neighbors.append(dfs(neighbor))

        #     return clone


        # return dfs(node)

        if not node:
            return None


        clones = {}

        clones[node] = Node(node.val)
        
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:

                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]

