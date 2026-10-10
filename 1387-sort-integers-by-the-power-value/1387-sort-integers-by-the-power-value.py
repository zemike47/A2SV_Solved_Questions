class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        memo = {}

        def countPowerValue(x):
            
            if x in memo:
                return memo[x]
            
            if x == 1:
                return 0
            
            if x % 2 == 1:
                count = 1 + countPowerValue(3 * x + 1)
            
            if x % 2 == 0:
                count =  1 + countPowerValue(x // 2)

            memo[x] = count
            return count
        
        hash_map = {}

        

        for x in range(lo,hi+1):

      
            count = countPowerValue(x)
            memo[x] = count

            hash_map[x] = count
        
        hash_map = dict(sorted(hash_map.items(),key= lambda item: item[1]))

        
        i = 0
        for key , value in hash_map.items():
            i += 1

            if i == k:
                return key
