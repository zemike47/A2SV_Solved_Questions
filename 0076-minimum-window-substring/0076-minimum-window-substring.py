from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        t_count = Counter(t)
        
        need = len(t_count)
        have = 0

        min_len = float("inf")
        left = 0

        window = defaultdict(int)
        result = ""

        for right in range(n):
            char = s[right]
            window[char] += 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                
                left_char = s[left]
                window[left_char] -= 1



                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1
            
                left += 1
        
        return result




