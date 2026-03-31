class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = set()
        n = len(pattern)

        def backtrack(curr):
            if len(curr) == n + 1:
                
                return curr

            for k in range(1,10):
                if k in used:
                    continue

                if curr:
                    if pattern[len(curr) - 1] == 'I' and curr[-1] >= k:
                        continue
                    if pattern[len(curr) - 1] == 'D' and curr[-1] <= k:
                        continue
                
                used.add(k)
                curr.append(k)

                ans = backtrack(curr)

                if ans:
                    return ans
                
                used.remove(k)
                curr.pop()

        result = backtrack([])

        return "".join(map(str,result))
                
