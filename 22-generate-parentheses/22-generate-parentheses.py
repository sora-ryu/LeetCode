class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Return sends a specified value back to its caller
        # whereas Yield can produce a sequence of values.
        
        # n = 3
        # lllrrr / llrlrr / llrrlr / lrllrr / lrlrlr
        
        ans = []
        def generate(p, left, right, ans):
            
            if right < left:
                return
            if not left and not right:
                ans.append(p)
                return
            if left:
                generate(p + '(', left-1, right, ans)
            if right:
                generate(p + ')', left, right-1, ans)
            
                
        generate('', n, n, ans)
        
        return ans
            
        