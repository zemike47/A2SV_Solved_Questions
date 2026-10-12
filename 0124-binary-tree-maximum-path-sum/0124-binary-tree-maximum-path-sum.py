# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        
        max_val = float("-inf")

        def dfs(node):
            nonlocal max_val

            if not node:
                return 0

            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))

            max_val = max(max_val,node.val + left + right)
            
            return node.val + max(left, right)

        dfs(root)

        return max_val