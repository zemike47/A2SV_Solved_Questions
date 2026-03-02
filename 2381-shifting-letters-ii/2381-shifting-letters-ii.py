class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0]*(n)

        for l,r,k in shifts:
            if k == 0:
                prefix[l] -= 1

                if r+1 < n:
                    prefix[r+1] += 1
            else:
                prefix[l] += 1

                if r + 1 < n:
                    prefix[r+1] -= 1
        print(prefix)
        
        
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1] 
        
        print(prefix)

        ans = []
        
        for i in range(len(s)):
            print()
            new_char = (ord(s[i]) - ord('a') + prefix[i]) % 26
            ans.append(chr(ord('a') + new_char))
               
        return "".join(ans)

            


            


            


            




