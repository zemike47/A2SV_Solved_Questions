# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def findMin(node):
            while node.left != None:
                node = node.left
            
            return node

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)

        else:
            if not root.left and not root.right:
                return None
            
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
            succesor = findMin(root.right)
            root.val = succesor.val
            root.right = self.deleteNode(root.right,succesor.val)

            
        return root

            
            
