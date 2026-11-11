# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '[]'

        result = []

        def preorder(node):
            if not node:
                return
            
            
            result.append(str(node.val))

            preorder(node.left)
            preorder(node.right)
            
        
        preorder(root)
        return ",".join(result)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == '[]':
            return None
        
        values = data.split(",")
        print(values)
        index = 0

        def dfs(lower,upper):
            nonlocal index

            if index >= len(values):
                return None

            val = int(values[index])

            if val < lower or val > upper:
                return None
            index += 1
           
            node = TreeNode(int(val))

            node.left = dfs(lower,val)
            node.right = dfs(val,upper)

            return node

        return dfs(float("-inf"),float("inf"))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans