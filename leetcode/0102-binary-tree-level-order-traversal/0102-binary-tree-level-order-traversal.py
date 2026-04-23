# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque()

        queue.append(root)
        res = []
        level = []

        
    
        level.append(root.val)
        # print(level)
        res.append(level)

        while queue:
            level = []
            # node = queue.popleft()
            # level.append(node)
            # print(node.val,end="")

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)

                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)

            # print(len(res))
            if len(level) != 0:
                # print(res)
                res.append(level)

        # print(res)
        return res

        
