class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordDict_set = set(wordDict)
        sentences = []
        def backtrack(start,sentence):
            if start == len(s):
                sentences.append(sentence.copy())
                return
            
            for i in range(start,len(s)):
                if s[start:i+1] in wordDict_set:
                    sentence.append(s[start:i+1])
                    backtrack(i+1,sentence)
                    sentence.pop()

        backtrack(0,[])

        if not sentences:
            return  []
        
        ans = []

        for sentence in sentences:
            ans.append(" ".join(sentence))
        
        return ans





        