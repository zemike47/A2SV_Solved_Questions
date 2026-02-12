class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)

        c = dict(sorted(c.items(),key = lambda x:(-x[1],x[0])))

        S = ""

        print(c)
        for key , value in c.items():
            S += key * value
        
        return S