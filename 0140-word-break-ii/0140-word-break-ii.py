class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []

        words = set(wordDict)
        

        def backtrack(start,curr):
            if start == n:
                res.append(" ".join(curr))
                return


            for i in range(start,n):
                word = s[start:i+1]

                if word in words:
                    curr.append(word)
                    backtrack(i+1,curr)
                    curr.pop()


        
        backtrack(0,[])

        return res

