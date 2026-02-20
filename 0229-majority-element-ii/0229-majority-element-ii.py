class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)

        ans = []

        n = len(nums) / 3

        for key,value in cnt.items():
            if value > n:
                ans.append(key)
        
        return ans
