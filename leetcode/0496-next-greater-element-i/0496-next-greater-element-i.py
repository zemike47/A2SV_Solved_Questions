class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        hashmap = {}

        for i in range(len(nums2)):
            if stack:
                top = stack[-1] 

            while stack and top < nums2[i]:
                hashmap[top] = nums2[i]
                stack.pop() 

                if stack:
                    top = stack[-1]   
            
            stack.append(nums2[i])

        ans = []

        for n in nums1:
            if n in hashmap:
                ans.append(hashmap[n])
            else:
                ans.append(-1)
        
        return ans



        

            
