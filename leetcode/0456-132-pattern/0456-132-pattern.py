class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_element = float("inf")

        for i in range(len(nums)):

            while stack and nums[i] >= stack[-1][1]:
                stack.pop()

            if stack and nums[i] > stack[-1][0]:
                return True

            stack.append((min_element,nums[i]))
            min_element = min(min_element,nums[i])



        return False

