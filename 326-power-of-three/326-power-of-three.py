class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Special cases
        if n == 0:
            return False
        elif n == 1:
            return True
        
        # Recursively divide by three until n becomes smaller or equal to 3.
        if n > 3:
            return self.isPowerOfThree(n / 3)
        
        if n == 3:
            return True
        
        return False