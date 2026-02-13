class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        negtive_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    negtive_count += 1
        
        return negtive_count
