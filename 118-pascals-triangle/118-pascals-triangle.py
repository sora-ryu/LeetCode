class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Base cases: numRows = 1 or 2
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        # Apply Pascal's triangle principles when numRows >= 3
        answer = [[1], [1,1]]
        for i in range(numRows - 2):
            inner_list = [1]
            for j in range(len(answer[-1])-1):
                inner_list.append(answer[-1][j] + answer[-1][j+1])
            inner_list.append(1)
            answer.append(inner_list)
        return answer
        