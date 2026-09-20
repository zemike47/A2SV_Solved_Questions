class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandCenter(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            

            return right - left  - 1
        
        start = 0
        end  = 0
        max_length = 1

        for i in range(len(s)):

            l1 = expandCenter(i,i)
            l2 = expandCenter(i,i+1)

            length = max(l1,l2)

            if length > max_length:
                if l1 >= l2:
                    start = i - (length // 2)
                    end = i + (length // 2)
                else:
                    start = i - (length // 2) + 1
                    end = i + (length // 2)
                
                max_length = length

        
        return s[start:end+1]








