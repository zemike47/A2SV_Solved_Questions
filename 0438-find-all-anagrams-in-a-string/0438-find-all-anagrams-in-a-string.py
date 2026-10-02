class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        from collections import Counter,defaultdict

        p_count = Counter(p)
        window = defaultdict(int)

        for i in range(len(p)):
            window[s[i]] += 1

        result = []

        if window == p_count:
            result.append(0)

        left = 0

        for right in range(len(p),len(s)):
            window[s[right]] += 1

            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]] 
            
            left += 1

            if window == p_count:
                result.append(left)
            
            
        return result






        