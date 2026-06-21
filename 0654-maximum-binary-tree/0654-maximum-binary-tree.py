# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        
        def build(arr):
            if not arr:
                return None

            mx = max(arr)
            idx = arr.index(mx)

            root = TreeNode(mx)

            root.left = build(arr[:idx])
            root.right = build(arr[idx + 1:])

            return root

        return build(nums)