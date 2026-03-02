class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = [0] * len(shifts)


        accumulator = 0
        for i in range(len(shifts)-1,-1,-1):
            accumulator += shifts[i]
            prefix[i] += accumulator

        ans = []

        print(prefix)


        for i in range(len(s)):
            new_char = (ord(s[i]) - ord('a') + prefix[i]) % 26
            print(new_char)
            ans.append(chr(ord('a') + new_char))

        return "".join(ans)

        


            

