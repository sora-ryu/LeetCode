class Solution:
    def isHappy(self, n: int) -> bool:
        
        ans = set()
        
        while n != 1:
            sum_squares = 0
            # Get each digits via converting int -> str -> int (inner loop)
            for digit in str(n):
                sum_squares += (int(digit)) ** 2
            print(sum_squares)
            if sum_squares in ans:
                return False
            else:
                ans.add(sum_squares)
                n = sum_squares
            print(ans)
        
        return True