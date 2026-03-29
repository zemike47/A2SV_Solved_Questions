class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        curr = []

        def backtrack(idx):
            if idx == n:
                return len(curr) >= 2


            for i in range(idx,n):
                val = int(s[idx:i+1])

                if len(curr) == 0 or val == curr[-1] - 1:
                    curr.append(val)

                    if backtrack(i+1):
                        return True
                        
                    curr.pop()
        
            return False

        return backtrack(0)
        
