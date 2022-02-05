class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return x ** n
        
#         # Time Limited Exceeded
#         ans = 1
#         for _ in range(abs(n)):
#             ans *= x
        
#         return ans if n > 0 else 1/ans