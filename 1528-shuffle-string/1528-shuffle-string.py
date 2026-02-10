class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        
        t = [""] * len(s)

        for i in range(len(indices)):
            t[indices[i]] = s[i]
        
        t = "".join(t)

        
        return t


