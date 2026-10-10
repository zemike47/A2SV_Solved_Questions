class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def countPowerValue(x):
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x  + 1

                count += 1
            
            return count
        
        hash_map = {}

        for x in range(lo,hi+1):

            count = countPowerValue(x)

            hash_map[x] = count
        
        hash_map = dict(sorted(hash_map.items(),key= lambda item: item[1]))

        
        i = 0
        for key , value in hash_map.items():
            i += 1

            if i == k:
                return key
