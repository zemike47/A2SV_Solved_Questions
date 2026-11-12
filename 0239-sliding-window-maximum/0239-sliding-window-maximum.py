class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = []
        queue = deque()
        

        for right in range(n):

            if queue and queue[0] <= right - k:
                queue.popleft()
            
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()

            queue.append(right)
            
            if right >= k-1:
                result.append(nums[queue[0]])

            
        return result
            
            


            

