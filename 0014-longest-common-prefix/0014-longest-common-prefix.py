class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs)

        for i in range(len(prefix)):
            for ch in strs:
                if prefix[i] != ch[i]:
                    return prefix[:i]
        
        return prefix


         