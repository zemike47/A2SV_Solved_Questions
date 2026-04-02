class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(path):
            count = 0

            for c in path:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1

                    if count < 0:
                        return False
            return count == 0

        res = set()
        mx = 0
    
        def backtrack(i,path):
            nonlocal mx, res

            if i == len(s):
                if isValid(path):
                    if len(path) > mx:
                        res = set()
                        mx = len(path)
                        
                    if len(path) == mx:
                        res.add(path)

                return


            if s[i] in "()":
                backtrack(i+1,path)
            backtrack(i+1,path + s[i])
        backtrack(0,"")

        return list(res)

        
        
    
