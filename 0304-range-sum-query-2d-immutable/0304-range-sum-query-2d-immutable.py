class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])

        self.prefixsum = [[0] * (n+1) for _ in range(m+1)]

        for r in range(m):
            for c in range(n):
                self.prefixsum[r+1][c+1] = matrix[r][c] + self.prefixsum[r][c+1] + self.prefixsum[r+1][c] - self.prefixsum[r][c] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefixsum
        return ( p[row2+1][col2+1] - p[row1][col2+1] - p[row2 + 1][col1] + p[row1][col1] )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)