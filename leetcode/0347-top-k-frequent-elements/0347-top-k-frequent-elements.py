class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = Counter(nums)
        ans = []

        while k:
            max_freq = float("-inf")
            KEY = None

            for num,freq in hash_map.items():
                if freq > max_freq:
                    max_freq = freq
                    KEY = num
           
            
            ans.append(KEY)
            del hash_map[KEY]
            k -= 1
        
        return ans
            

            



   