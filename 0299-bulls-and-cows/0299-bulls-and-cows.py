class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls = 0 

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        
        count = 0

        s = Counter(secret)
        g = Counter(guess)

        for key in s:
            if key in g:
                count = count + min(s[key],g[key])
            
        cows = count - bulls

        
        return f"{bulls}A{cows}B"
            




    