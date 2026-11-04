class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
                max_depth = max(max_depth,len(stack))
            elif char == ")":
                stack.pop()
        
        return max_depth