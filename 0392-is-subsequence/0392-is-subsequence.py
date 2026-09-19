class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        positions = {}

        for i, char in enumerate(t):
            if char not in positions:
                positions[char] = []
            positions[char].append(i)
        

        current = -1

        for char in s:
            if char not in positions:
                return False
            
            arr = positions[char]

            left = 0
            right = len(arr)

            while left < right:
                mid = (left+right) // 2

                if arr[mid] <= current:
                    left = mid + 1
                
                else:
                    right = mid

            
            if left == len(arr):
                return False
            
            current = arr[left]
        
        return True

