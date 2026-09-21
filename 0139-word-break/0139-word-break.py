class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        wordDict = set(wordDict)

        for i in range(1,n+1):
            
            for j in range(i):
                if s[j:i] in wordDict:
                    dp[i] = dp[j] or dp[i]
                    
        
        print(dp)
        return dp[n]

    

