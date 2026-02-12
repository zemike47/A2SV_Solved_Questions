class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        new_matrix = [[0] * rows for _ in range(cols)]


        for i in range(cols):
            for j in range(rows):
                new_matrix[i][j] = matrix[j][i]

        return new_matrix





        