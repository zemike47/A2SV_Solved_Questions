class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        result = []
     

        for i in range(1,numRows+1):
            row = [1] * i

            for j in range(1,i-1):
                row[j] = result[i-2][j-1] + result[i-2][j]

            result.append(row)

        return result

