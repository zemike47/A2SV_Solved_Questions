class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        strs.sort()

        ans = ""
        i = 0

        while True:
            if i < len(strs[0]):
                w = strs[0][i]
                for st in strs[1:]:
                    if i < len(st) and st[i] == w:
                        continue

                    else:
                        return ans 
                
                ans += w
                i += 1
            else:
                return ans 
        
        return ans 
    
        


