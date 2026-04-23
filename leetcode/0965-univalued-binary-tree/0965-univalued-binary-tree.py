# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append(root)

        val = root.val

        while queue:
            node = queue.popleft()

            if node.right:
                if node.right.val == val:
                    queue.append(node.right)
                else:
                    return False
            
            if node.left:
                if node.left.val == val:
                    # queue.append(node.right)
                    queue.append(node.left)
                else:
                    return False
                # queue.append(node.left)
        return True
            

            

