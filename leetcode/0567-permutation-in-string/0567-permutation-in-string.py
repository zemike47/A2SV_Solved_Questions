class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        target = Counter(s1)

        for i in range(n - m + 1):
            if Counter(s2[i:i + m]) == target:
                return True

        return False
            
        
            
                
