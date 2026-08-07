class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz",
        }


        result = []

        def backtrack(start,path):
            if len(path) == len(digits):
                result.append("".join(path))
                return

            
            for i in range(len(hash_map[digits[start]])):

                path.append(hash_map[digits[start]][i])

                backtrack(start+1,path)

                path.pop()

        backtrack(0,[])

        return result



        