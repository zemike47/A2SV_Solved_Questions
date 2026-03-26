# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(pre,inO):
            if not pre or not inO:
                return 

            root = TreeNode(pre[0])
            idx = inO.index(pre[0])

            LinO = inO[:idx]
            RinO = inO[idx+1:]


            Lpre = pre[1:idx + 1]
            Lpre = pre[idx + 1:]



            root.left = build(Lpre,LinO)
            root.right = build(Rpre,rinO)
        
        return build(preorder,inorder)# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(pre,inO):
            if not pre or not inO:
                return None

            root = TreeNode(pre[0])
            idx = inO.index(pre[0])

            LinO = inO[:idx]
            RinO = inO[idx+1:]


            Lpre = pre[1:idx + 1]
            Rpre = pre[idx + 1:]



            root.left = build(Lpre,LinO)
            root.right = build(Rpre,RinO)

            return root

        
        
        return build(preorder,inorder)




        




        