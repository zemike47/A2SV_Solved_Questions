class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        result = []
     

        for i in range(1,rowIndex+2):
            row = [1] * i

            for j in range(1,i-1):
                row[j] = result[i-2][j-1] + result[i-2][j]

            result.append(row)


        return result[rowIndex]