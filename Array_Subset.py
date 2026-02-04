#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        
        a.sort()
        b.sort()
        
        l,r= 0,0
        
        while l < len(a) and r < len(b):
            if a[l] == b[r]:
                r += 1
                l += 1
            elif a[l] > b[r]:
                return False
            else:
                l += 1
        
        
        
        return r >= len(b)
                
                
    
    
    
    
