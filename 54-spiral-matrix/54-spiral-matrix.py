class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        find = []
        rows, columns = len(matrix), len(matrix[0])
        i_start, j_start = 0, 0
        i_end, j_end = rows-1, columns-1
        # 1st row -> last column -> last row -> first column -> 2nd row -> ...
        while len(find) != (rows * columns):
            
            for j in range(j_start, j_end+1):
                find.append(matrix[i_start][j])
            i_start += 1
            
            if len(find) == rows * columns:
                break
            
            for i in range(i_start, i_end+1):
                find.append(matrix[i][j_end])
            j_end -= 1
            
            if len(find) == rows * columns:
                break
                
            for j in range(j_end, j_start-1, -1):
                find.append(matrix[i_end][j])
            i_end -= 1
            
            if len(find) == rows * columns:
                break
                
            for i in range(i_end, i_start-1, -1):
                find.append(matrix[i][j_start])
            j_start += 1
            
            print(find)
            
        return find
        