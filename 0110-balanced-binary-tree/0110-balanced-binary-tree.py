class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        if not root:
            return True

        isBalanced = True

        def isB(root):
            nonlocal isBalanced

            if not root:
                return 0

            left = isB(root.left)
            right = isB(root.right)

            if abs(right - left) > 1:
                isBalanced = False

            return 1 + max(left, right)

        isB(root)

        return isBalanced