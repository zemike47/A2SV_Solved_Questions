class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        left_max_arr = [0] * n
        right_max_arr = [0] * n

        left_max_arr[0] = height[0]
        right_max_arr[n-1] = height[n-1]


        for i in range(1,n):
            left_max_arr[i] = max(height[i],left_max_arr[i-1])

        for i in range(n-2,-1,-1):
            right_max_arr[i] = max(height[i],right_max_arr[i+1])
        
        water = 0

        # print(left_max_arr)
        # print(right_max_arr)


        for i in range(n):
            water += min(left_max_arr[i] , right_max_arr[i]) - height[i]

        return water
