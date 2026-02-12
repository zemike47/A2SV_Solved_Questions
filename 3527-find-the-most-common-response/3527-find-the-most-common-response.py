class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        hash_map = {}

        for i in range(len(responses)):
            hash_map[i] = list(set(responses[i]))
        
        r = [v  for values in hash_map.values() for v in values]

        
        c = Counter(r)

        c= list(sorted(c.items(),key = lambda x: (-x[1],x[0])))

        return c[0][0]



        
        






        