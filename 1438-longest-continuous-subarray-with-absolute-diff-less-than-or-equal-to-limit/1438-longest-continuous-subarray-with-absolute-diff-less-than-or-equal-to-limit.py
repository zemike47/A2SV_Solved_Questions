class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        maxdeque = deque()
        mindeque = deque()

        left = 0
        ans = 0

        for i in range(len(nums)):

            while maxdeque and  nums[i] > maxdeque[-1]:
                maxdeque.pop()
            maxdeque.append(nums[i])

            while mindeque and  nums[i] < mindeque[-1]:
                mindeque.pop()
            mindeque.append(nums[i])

            while maxdeque[0] - mindeque[0] > limit:
                num = nums[left]
                if maxdeque[0] == num:
                    maxdeque.popleft()
                elif mindeque[0] == num:
                    mindeque.popleft()

                left += 1 
            ans = max(ans,i - left + 1)

        return ans





