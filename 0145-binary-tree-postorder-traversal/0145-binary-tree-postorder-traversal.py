# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []

        result = []
        stack = [root]
        
        while stack:
            root = stack.pop()
            result.append(root.val)

            
            if root.left:
                stack.append(root.left)
            
            if root.right:
                stack.append(root.right)
            
        
        return result[::-1]

       

