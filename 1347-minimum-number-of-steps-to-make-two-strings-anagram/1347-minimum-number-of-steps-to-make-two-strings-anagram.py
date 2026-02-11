class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)

        counter_t = Counter(t)

        count = 0


        for key in set(t):
            if counter_t[key] > counter_s[key]:
                count += (counter_t[key] - counter_s[key]) 
              

            
            
        
        return count

