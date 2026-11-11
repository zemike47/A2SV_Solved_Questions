# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'

        result = []

        def preOrderwithNullMarker(node):
            if not node:
                result.append("null")
                return
            
            result.append(str(node.val))

            preOrderwithNullMarker(node.left)
            preOrderwithNullMarker(node.right)
            
        
        preOrderwithNullMarker(root)
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        
        values = data.split(",")
        index = 0

        def dfs():
            nonlocal index

           
            val = values[index]

            if val == "null":
                index += 1

                return None
            index += 1

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node




        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))