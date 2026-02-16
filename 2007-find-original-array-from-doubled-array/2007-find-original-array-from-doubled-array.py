class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()

        c = Counter(changed)

        res = []

        for x in changed:
            if c[x] == 0:
                continue
            
            if c[2 * x] == 0:
                return []
            
            res.append(x)
            c[x] -= 1
            c[2*x] -= 1
        
        return res
            




