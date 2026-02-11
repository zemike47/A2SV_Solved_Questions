class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter_nums = Counter(nums)

        for freq in counter_nums.values():
            if freq >= 2:
                return True
        else:
            return False
        
        