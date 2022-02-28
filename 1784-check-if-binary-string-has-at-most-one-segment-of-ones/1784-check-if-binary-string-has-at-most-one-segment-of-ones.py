class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        # Without leading zeros
        # => s doesn't start with 0
        # => If "01" exists, it means that there is more than one segments of ones.
        return False if "01" in s else True
        