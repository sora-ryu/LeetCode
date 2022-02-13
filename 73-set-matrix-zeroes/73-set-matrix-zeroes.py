class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        print(rows, cols)
        
        for row in rows:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
                
        print(matrix)