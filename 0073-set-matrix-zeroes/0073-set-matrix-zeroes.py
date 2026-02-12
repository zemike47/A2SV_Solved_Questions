class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zeros_rows = set()
        zeros_cols = set()


        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros_rows.add(i)
                    zeros_cols.add(j)

        
        for i in zeros_rows:
            for j in range(cols):
                
                matrix[i][j] = 0

        for j in zeros_cols:
            for i in range(rows):
                
                matrix[i][j] = 0         



        

        print(matrix)


        return matrix
        
        