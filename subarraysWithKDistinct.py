class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostk(k):
            left = 0
            freq_map = defaultdict(int)
            ans = 0

            for right in range(len(nums)):
                freq_map[nums[right]] += 1

                while len(freq_map) > k:
                    freq_map[nums[left]] -= 1

                    if freq_map[nums[left]] == 0:
                        del freq_map[nums[left]]

                    left += 1
                

                
                ans += right - left + 1

            return ans

        n1 = atmostk(k)
        n2 = atmostk(k-1)

        result = n1 -n2

        return result

            
        
            

                

                

                 






            
