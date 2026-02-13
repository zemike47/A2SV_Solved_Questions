
class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        counter = Counter(nums)
        dom, total_count = counter.most_common(1)[0]
        
        count_left = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == dom:
                count_left += 1
            
            len_left = i + 1
            len_right = n - len_left
            count_right = total_count - count_left
            
            if count_left * 2 > len_left and count_right * 2 > len_right:
                return i
        
        return -1
