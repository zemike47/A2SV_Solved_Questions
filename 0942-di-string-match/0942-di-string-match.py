class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low,high = 0 , len(s)

        ans = []
   
        for ch in s:
            # print(ch)
            if ch == "I":
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1

        if s[-1] == "I":
            ans.append(low)
        else:
            ans.append(high)
        
        return ans 