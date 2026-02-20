class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""

        cnt = Counter(s)

        print(cnt)


        for i in range(len(order)):
            if order[i] in s:
                ans += (order[i] * (cnt[order[i]]))
        
        for key,value in cnt.items():
            if key not in ans :
                ans += (key * value)
        
        return ans