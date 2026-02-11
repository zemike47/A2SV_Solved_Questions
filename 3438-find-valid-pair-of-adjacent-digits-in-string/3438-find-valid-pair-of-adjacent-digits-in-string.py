class Solution:
    def findValidPair(self, s: str) -> str:
        valid_pair = Counter(s)



        for i in range(len(s)-1):
          
            if s[i] != s[i+1] and valid_pair[s[i]] == int(s[i]) and valid_pair[s[i+1]] == int(s[i+1]):
                
                new_S = ""
                new_S += s[i]
                new_S += s[i+1]

                return new_S
        else:
            return ""
        

        

