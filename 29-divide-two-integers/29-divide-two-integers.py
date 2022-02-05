class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (dividend < 0) is (divisor < 0):
            sign = 1
        else:
            sign = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            curr_divisor, num_divisors = divisor, 1
            while dividend >= curr_divisor:
                dividend -= curr_divisor
                res += num_divisors
                
                # Use bitwise operation
                # << 1: move right 1 bit (divide by 2)
                # >> 1: move left 1 bit (multiply by 2)
                curr_divisor = curr_divisor << 1
                num_divisors = num_divisors << 1
				
		
        return min(max(-2147483648, sign * res), 2147483647)
        
#         # Time Limit Exceeded
#         # Define the sign
#         if dividend == 0:
#             return 0
#         elif dividend > 0 and divisor > 0:
#             sign = 1
#         elif dividend > 0 and divisor < 0:
#             sign = -1
#         elif dividend < 0 and divisor > 0:
#             sign = -1
#         else:
#             sign = 1
        
#         ans, count = 0, 1
#         for i in range(abs(dividend)):
#             if count == abs(divisor):
#                 ans += 1
#                 count = 0
#             count += 1
#         return sign * ans

