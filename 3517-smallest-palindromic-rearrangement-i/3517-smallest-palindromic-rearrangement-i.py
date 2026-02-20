class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        cnt = Counter(s)
        cnt = dict(sorted(cnt.items()))

        middle = ""
        left = []

        for key,value in cnt.items():
            if value % 2 == 1:
                middle += key
        
        for key,value in cnt.items():
            left.append(key * (value//2))
        
        left = "".join(left)
        right = left[::-1]


        return left + middle + right

        
        
            
