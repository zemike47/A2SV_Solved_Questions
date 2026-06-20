# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
    #     class Solution:
    # def maxSumBST(self, root):
        ans = 0

        def dfs(node):
            nonlocal ans

            # Empty tree is a BST
            if not node:
                return (True, float('inf'), float('-inf'), 0)

            leftBST, leftMin, leftMax, leftSum = dfs(node.left)
            rightBST, rightMin, rightMax, rightSum = dfs(node.right)

            # Check if current subtree is a BST
            if (
                leftBST
                and rightBST
                and leftMax < node.val < rightMin
            ):
                currSum = leftSum + rightSum + node.val

                ans = max(ans, currSum)

                return (
                    True,                       # is BST
                    min(leftMin, node.val),    # min value
                    max(rightMax, node.val),   # max value
                    currSum                    # subtree sum
                )

            # Not a BST
            return (False, 0, 0, 0)

        dfs(root)
        return ans


        