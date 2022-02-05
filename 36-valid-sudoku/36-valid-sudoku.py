class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    seen += [(num,j),(i,num),(i//3,j//3,num)] 
                    # (num,j) - Column
                    # (i,num) - Row
                    # (i/3,j/3,num) - 3x3 sub-box: 0,1,2 divide by 3 -> all 0
        print(seen)
        return len(seen) == len(set(seen))  # Return false if two lengths are different which means that duplication occured.