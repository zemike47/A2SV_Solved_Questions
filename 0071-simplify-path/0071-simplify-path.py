class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        list_s = path.split('/')

        print(list_s)

        for c in list_s:
            if c == "..":
                if stack:
                    stack.pop()
            elif c == "." or c == "/" or c == "":
                continue

            else:
                stack.append(c)
        
        return "/"+"/".join(stack)


      
