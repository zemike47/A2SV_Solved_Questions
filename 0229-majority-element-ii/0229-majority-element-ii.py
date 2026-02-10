class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq = len(nums) / 3

        c = Counter(nums)
        ans = []

        for key , values in c.items():
            if values > freq:
                ans.append(key)
        
        return ans

