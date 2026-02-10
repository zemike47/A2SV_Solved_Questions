class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        st = Counter(s)

        for i in range(len(s)):
            if st[s[i]] == 1:
                return i
        else:
            return -1
