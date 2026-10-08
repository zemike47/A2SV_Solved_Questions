# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        result = []

        from collections import deque

        queue = deque([root])

        while queue:
            curr = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(curr[-1])
        
        return result
            