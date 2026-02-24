class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cntr_p = Counter(p)

        k = len(p)
        ans  = []
        window = Counter(s[:len(p)])

       

        if cntr_p == window:
            ans.append(0)

      

        left = 0

        for right in range(len(p),len(s)):
            window[s[right]] += 1
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]
            
            if cntr_p == window:
                ans.append(left+1)

            left += 1
        
        return ans