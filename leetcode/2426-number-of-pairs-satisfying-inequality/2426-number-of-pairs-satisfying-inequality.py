class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]
        cnt = 0
        def merge(leftarr, rightarr):

            l = 0
            r = 0
            arr = []
            while l < len(leftarr) and r < len(rightarr):
                if leftarr[l] <= rightarr[r]:
                    arr.append(leftarr[l])
                    l += 1
                else:
                    arr.append(rightarr[r])
                    r += 1
            arr.extend(leftarr[l:])
            arr.extend(rightarr[r:])
            return arr
        # print(nums1)
        def mergesort(left, right, arr):
            nonlocal cnt
            if left == right:
                return [arr[left]]

            
            mid = left + (right - left)//2

            leftarr = mergesort(left, mid, arr)
            rightarr = mergesort(mid + 1, right, arr)
            # print(leftarr, rightarr)
            
            j = 0
            for each in rightarr:
                while j < len(leftarr) and each + diff >= leftarr[j]:
                    j += 1
                # print(j)
                cnt += j



            return merge(leftarr, rightarr)
        
        print(mergesort(0, len(nums1) - 1, nums1))
        return cnt