class Solution:
    def isPalindrome(self, s: str) -> bool:

        pharse = ""

        for c in s:
            if c.isalnum():
                pharse += c
        
        left , right = 0, len(pharse) - 1

        while left < right:
            if pharse[left].lower() != pharse[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
        