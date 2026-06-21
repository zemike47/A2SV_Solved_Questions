# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val

            paths = prefix[currSum - targetSum]
            
            prefix[currSum] += 1

            paths += dfs(node.left, currSum)
            paths += dfs(node.right, currSum)

            prefix[currSum] -= 1 

            return paths

        return dfs(root, 0)