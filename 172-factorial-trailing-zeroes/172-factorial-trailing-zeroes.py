class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ans, factorial = 0, 1
        for i in range(1, n+1):
            factorial *= i
        
        
        for j in str(factorial)[::-1]:
            if j != '0':
                break
            ans += 1
        
        return ans
        