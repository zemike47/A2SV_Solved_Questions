# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        n = len(postorder)
        hashmap = {}

        for i,val in enumerate(postorder):
            hashmap[val] = i

        def build(i1,i2,j1):
            if i1 > i2 :
                return None

            root = TreeNode(preorder[i1])
            
            if i1 != i2:
                last_val = preorder[i1+1]
                mid = hashmap[last_val]

                left_Size = mid + 1 - j1

                root.left = build(i1+1,i1+left_Size,j1)
                root.right = build(i1+left_Size+1,i2,mid+1)

            return root
        
        return build(0,n-1,0)


