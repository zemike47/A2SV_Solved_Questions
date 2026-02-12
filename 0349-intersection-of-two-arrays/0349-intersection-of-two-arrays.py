class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        n2_set = set(nums2)

        for n in nums1:
            if n in n2_set:
                ans.append(n)
        
        n1_set = set(nums1)

        for n in nums2:
            if n in n1_set:
                ans.append(n)
        
        ans = list(set(ans))
        
        return ans

