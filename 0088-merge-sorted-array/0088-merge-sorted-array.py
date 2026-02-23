class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
              

        ptr = m + n - 1

        i,j = m-1 , n - 1

        while  i>= 0 and j >= 0:

            if nums2[j] >= nums1[i]:
                nums1[ptr] = nums2[j]
                j -= 1
                ptr -= 1
            else:
                nums1[ptr] = nums1[i]
                i -= 1
                ptr -= 1
        
        
        
        if j >= 0:
            while j >= 0:
                nums1[ptr] = nums2[j]
                j -= 1
                ptr -= 1
        




    
        


