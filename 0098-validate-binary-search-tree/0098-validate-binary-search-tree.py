# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def check(node,lower,upper):
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False

            if not check(node.left,lower,node.val):
                return False
            if not check(node.right,node.val,upper):
                return False
        
            return True
        
        return check(root,float("-inf"),float("inf"))
