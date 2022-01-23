class Solution:
    def climbStairs(self, n: int) -> int:
        # It's Fibonacci Numbers
        
        # Time Limit Exceeded
#         def fibo(n):
#             # Base cases
#             if n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
        
#             return fibo(n-2) + fibo(n-1)
        
#         return fibo(n)


        # 1, 2, 3, 5, 8, 13, ...
        # make above fibonacci numbers and return nth number
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        answer = [0, 1, 2]  # Base cases (n=0,1,2)
        
        for i in range(n-2):
            answer.append(answer[-1] + answer[-2])
        return answer[-1]