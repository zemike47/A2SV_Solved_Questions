class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        import collections

        window = collections.defaultdict(int)
        
        max_fruits = 0
        left = 0
        for right in range(len(fruits)):
            window[fruits[right]] += 1
            
            while len(window) > 2:
                window[fruits[left]] -= 1
                
                
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                
                left += 1
            
            max_fruits = max(max_fruits,right - left + 1)
        
        return max_fruits