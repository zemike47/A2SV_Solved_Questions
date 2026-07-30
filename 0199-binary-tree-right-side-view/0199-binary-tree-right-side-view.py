# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        def dfs(root,depth):
            nonlocal result

            if not root:
                return

            if len(result) == depth:
                result.append([])
            
            result[depth].append(root.val)

            dfs(root.left,depth+1)
            dfs(root.right,depth+1)

        
            return result

        dfs(root,0)

        rightSideView = []

        for lvl in result:
            rightSideView.append(lvl[-1])
            


        return rightSideView