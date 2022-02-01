class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # [::-1] to flip the matrix upside down and then zip to transpose it. It assigns the result back into A, so it's "in-place" in a sense
        
        # matrix: [[1,2,3],[4,5,6],[7,8,9]]
        # matrix[::-1] : [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        # matrix[:] = zip(*matrix)  => [[1,4,7],[2,5,8],[3,6,9]]
        matrix[:] = zip(*matrix[::-1])