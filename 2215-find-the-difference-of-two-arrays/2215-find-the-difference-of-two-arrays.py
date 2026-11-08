class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        result = []

        uniq1 = set()
        for num in nums1:
            if num not in set2:
                uniq1.add(num)
        
        uniq2 = set()
        for num in nums2:
            if num not in set1:
                uniq2.add(num)
        
        return[list(uniq1),list(uniq2)]


        