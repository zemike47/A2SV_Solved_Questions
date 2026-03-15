class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []

        n = len(nums)

        for i in range(n):

            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            if queue[0] <= i - k:
                queue.popleft()
  

            if i + 1 >= k:
                if queue:
                    ans.append(nums[queue[0]])
            
        return ans
