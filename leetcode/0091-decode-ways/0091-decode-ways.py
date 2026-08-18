class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n+1)
        dp[0] = 1


        for i in range(1,n+1):
           
            
            #take one digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            #take two digit

            if i>= 2:
                digit = int(s[i-2:i])

                if 10 <= digit <= 26:
                    dp[i] += dp[i-2]
            
        return dp[n]