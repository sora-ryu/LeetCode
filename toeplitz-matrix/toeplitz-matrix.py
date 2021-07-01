class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ans = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:  # Check whether each value is equal to the value of its top-left neighbor.
                    ans = False
                    break
        
        return ans