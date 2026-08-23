class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # step - 1 transpose matrix

        for r in range(len(matrix)):
            for c in range(r+1,len(matrix)):
                matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]

        #step 2 reverse row

        for row in matrix:
            row.reverse()

        
        
        
            