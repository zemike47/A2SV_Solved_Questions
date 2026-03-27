class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hash_map = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }

        ans = [] 

        def backtrack(start,path):
            if len(path) == len(digits):
                ans.append("".join(path))
                return

            for ch in range(len(hash_map[digits[start]])):

                path.append(hash_map[digits[start]][ch])

                backtrack(start+1,path)

                path.pop()

        backtrack(0,[])

        return ans
        