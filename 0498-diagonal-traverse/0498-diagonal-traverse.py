class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for key in range(m + n - 1):
            temp = []
            for i in range(m):
                j = key - i
                if 0 <= j < n:
                    temp.append(mat[i][j])
            
            if key % 2 == 0:
                temp.reverse()
            
            result.extend(temp)

        return result
