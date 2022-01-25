class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # s = s[::-1]
        # s = s.reverse()
        s[:] = s[::-1]
        
# Note:
# s[:] = s[::-1] is required NOT s = s[::-1] because you have to edit the list inplace.
# Under the hood, s[:] = is editing the actual memory bytes s points to, and s = points the variable name s to other bytes in the memory.

# (easiest except .reverse())