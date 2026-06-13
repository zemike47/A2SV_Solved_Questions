class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def can_ship(cap):
            days_used = 1
            curr_cap = 0

            for w in weights:

                if curr_cap + w > cap:
                    days_used += 1
                    curr_cap = w
                else:
                    curr_cap += w
                
            return days_used <= days
        
        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = (left + right) // 2

            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
            

