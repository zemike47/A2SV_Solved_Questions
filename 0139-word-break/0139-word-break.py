class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        wordDict_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for i in range(start,len(s)):
                if s[start:i+1] in wordDict_set:
                    if backtrack(i+1):
                        memo[start] = True
                        return True
            

            memo[start] = False
            return False

       
        return  backtrack(0)





        