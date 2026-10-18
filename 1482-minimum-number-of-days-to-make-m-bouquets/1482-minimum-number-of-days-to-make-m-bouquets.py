class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        

        def canMake(day):
            
            curr = 0
            bouquets = 0

            for i in range(len(bloomDay)):
                if day >= bloomDay[i]:
                    curr += 1
                else:
                    curr = 0

                if curr >= k:
                    bouquets += 1
                    curr = 0
            
            return bouquets >= m

        left = 0
        right = max(bloomDay) + 1
        
        can = False
        while left < right:
            mid = (left+right) // 2

            if canMake(mid):
                can = True
                right= mid
            else:
                left = mid + 1
        
        return left if can else - 1
        




