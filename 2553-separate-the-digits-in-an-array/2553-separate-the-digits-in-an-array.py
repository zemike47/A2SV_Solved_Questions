class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        s = ""

        for n in nums:
            num = str(n)

            s += num

        ans = []
        for c in s:
            num = int(c)
        
            ans.append(num)
        
        return ans


    
