class Solution:    
    def findUnion(self, a, b):
        # code here
        
        set_a = set(a)
        set_b = set(b)
        
        union = set_a | set_b
        
        return(list(union))
        
