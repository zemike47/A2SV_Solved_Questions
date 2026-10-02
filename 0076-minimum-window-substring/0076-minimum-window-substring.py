class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter,defaultdict

        t_count = Counter(t)
        need = len(t_count)
        have  = 0

        left = 0
        best_left = 0

        window = defaultdict(int)
        min_length = float("inf")
        

        for right in range(len(s)):
            window[s[right]] += 1
            char = s[right]

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:

                if right - left + 1 < min_length:
                    best_left = left
                    min_length = right - left + 1
                
                window[s[left]] -= 1
            
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

            
        
        if min_length == float("inf"):
            return ""

        return s[best_left:best_left + min_length]
        





