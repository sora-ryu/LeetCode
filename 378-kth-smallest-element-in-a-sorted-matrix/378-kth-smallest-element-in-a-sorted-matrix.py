class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # duplicated elements?
        # each array is already sorted
        # the lengths of each array are all the same?
        # the range of k?
        
        # Time complexity of sorting an array of size n^2 is O(n^2 * log n)
        # Space complexity is O(n^2)
        
        result = []
        # for each array in matrix:
        for array in matrix:  
            # add array into result_array
            result += array

        # sort the result_array
        result.sort()
        # return the kth element from it
        # note that the index starts with zero
        return result[k-1]
        