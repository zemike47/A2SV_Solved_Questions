class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        
        mid = num // 3
        low = mid - 1
        high = mid + 1

        ans = [low,mid,high]
      
        return ans

    
