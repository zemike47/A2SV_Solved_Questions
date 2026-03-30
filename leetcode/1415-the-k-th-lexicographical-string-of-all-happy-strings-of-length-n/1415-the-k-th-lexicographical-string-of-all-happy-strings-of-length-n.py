class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        char = ['a','b','c']
        happyStr = []



        def backtrack(curr):
            if len(curr) == n:
                happyStr.append(curr[:])
                return

            for i in range(3):
                if curr:
                    if curr[-1] == char[i]:
                        continue


                curr.append(char[i])

                backtrack(curr)

                curr.pop()
            

        backtrack([])

        happyStr.sort()

        print(happyStr)
        print(len(happyStr))


        if len(happyStr) > k-1:
            return "".join(happyStr[k-1])
        
        else:
            return ""
