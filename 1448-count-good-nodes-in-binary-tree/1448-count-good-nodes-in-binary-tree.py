# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root.left and not root.right:
                return 1

        count = 0
        
        def dfs(node,max_val):
            nonlocal count
            if not node.left and not node.right:
                if node.val >= max_val:
                    max_val = node.val
                    count += 1
                
                return 

            if node.val >= max_val:
                max_val = node.val
                count += 1
            
            if node.left:
                dfs(node.left,max_val)
            
            if node.right:
                dfs(node.right,max_val)
        

        dfs(root,root.val)
        return count
        

