class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        ans = []

        for key in nums_count:
            if nums_count[key] == 2:
                ans.append(key)
        
        return ans
