class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")
        children = [0] * k
        n = len(cookies)

        def backtrack(i):
            nonlocal ans
            if i == n:
                ans = min(ans,max(children))
                return

            for j in range(k):
                children[j]  += cookies[i]

                if max(children) < ans:
                    backtrack(i+1)

                children[j]  -= cookies[i]

                if children[j] == 0:
                    break

        backtrack(0)

        return ans

        

