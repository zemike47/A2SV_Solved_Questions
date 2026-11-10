class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        
        for p in path:
            if p == '':
                if not stack: 
                    stack.append(p)
            elif p == "..":
                stack.pop()
                if not stack:
                    stack.append("")
            elif p == ".":
                continue
            else:
                stack.append(p)
        
        if stack[-1] == '':
            stack.pop()
        

        return "/".join(stack) if stack else "/"
       