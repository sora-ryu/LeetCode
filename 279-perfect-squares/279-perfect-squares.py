class Solution:
    def numSquares(self, n: int) -> int:
        
        basic_squares = []   # Save perfect squares smaller than n
        
        for i in range(n+1):
            if sqrt(i).is_integer():
                basic_squares.append(i)
        
        dp = [i for i in range(n+1)]
        
        for i in range(len(dp)):
            for j in basic_squares:
                if i < j:
                    break
                dp[i] = min(dp[i-j]+1, dp[i])
        
        return dp[-1]
            
                    
        