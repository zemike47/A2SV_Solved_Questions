# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        level = 0
        queue = deque()
        if root:
            queue.append(root)



        while queue:
            for _ in range(len(queue)):
                root = queue[0]
                queue.popleft()

                if not root.left and not root.right:
                    return level + 1 

                if root.left:
                    queue.append(root.left)
                
                if root.right:
                    queue.append(root.right)
                
                
            
            
            level += 1
        
        return level