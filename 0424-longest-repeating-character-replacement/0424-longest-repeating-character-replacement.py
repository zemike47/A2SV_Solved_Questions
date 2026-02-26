class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        n = len(s)
        ans = float("-inf")
        hash_map = defaultdict(int)

        for right in range(n):
            hash_map[s[right]] += 1
            cur = (right - left + 1) - max(hash_map.values())
            while cur > k:
                hash_map[s[left]] -= 1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left += 1
                cur = (right - left + 1) - (max(hash_map.values()) if len(hash_map) > 0 else 0)
            
            ans = max(ans, (right - left + 1))
        
        return ans
    




    