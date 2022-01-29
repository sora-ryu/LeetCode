class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # built-in function: bin()
        return bin(n).count('1')