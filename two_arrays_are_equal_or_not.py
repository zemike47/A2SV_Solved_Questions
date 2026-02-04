from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        
        set_a = Counter(a)
        set_b = Counter(b)
        
        
        
        return set_a == set_b
        
        
        
