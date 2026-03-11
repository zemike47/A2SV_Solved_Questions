class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        # stack = []
        # max_area = 0
            

        # for i in range(len(heights)):
        #     while stack and heights[i] > heights[stack[-1]]:
                
        #         w = i - stack[-1] + 1
        #         h = min(heights[i],heights[stack[-1]])
        #         max_area = max(max_area,h * w)

        #         stack.pop()
            
        #     stack.append(i)
        #     w = i - stack[-1] + 1
        #     h = min(heights[i],heights[stack[-1]])
        #     max_area = max(max_area,h * w)
            
        
        
        n = len(heights)
        left = list(range(n))
        right = list(range(n))
        
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                left[i] = left[stack.pop()]
            stack.append(i)
        

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                right[i] = right[stack.pop()]
            stack.append(i)
        
        
        
        max_area = 0
        for i in range(n):
            ele = right[i] - left[i] + 1
            max_area = max(max_area, ele * heights[i])

        
        

        return max_area