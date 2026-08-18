class Solution:
    def longestPalindrome(self, s: str) -> str:

        # n = len(s)
        # dp = [[False]*n for _ in range(n)]

        # maxLen = 1
        # resIndex = 0

        # for i in range(n-1,-1,-1):
        #     for j in range(i,n):

        #         if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1] ) :

        #             dp[i][j] = True

        #             if maxLen < j - i + 1:
        #                 maxLen = j - i + 1
        #                 resIndex = i

        # return s[resIndex:resIndex+maxLen]

        resIndex = 0 
        max_length = 0

        for i in range(len(s)):
            # odd length
            l,r = i,i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    resIndex = l

                l -= 1
                r += 1
        
            # even length
            l,r = i,i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if  r - l + 1 > max_length:
                    max_length = r - l + 1
                    resIndex = l

                l -= 1
                r += 1

        return s[resIndex:resIndex+max_length]
            







        