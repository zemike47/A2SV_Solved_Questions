# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def deleteNode(root,key):
            if not root:
                return None
            
            if root.val < key:
                root.right = deleteNode(root.right,key)
            elif root.val > key:
                root.left = deleteNode(root.left,key)

            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                

                temp = minElement(root.right)
                root.val = temp.val

                root.right = deleteNode(root.right,temp.val)

            return root

        
        def minElement(node):
            curr = node

            while curr.left:
                curr = curr.left
            
            return curr
        
        return deleteNode(root,key)
        

