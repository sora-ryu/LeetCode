class Solution:
    def reverseBits(self, n: int) -> int:
        
        # 1st line in the loop: n & 1, we check if last bit of n is set, is it 1 or 0, ans << 1 we shift all bits that we already have in our answer to the left, so after this shifting the bit on the right is 0, + by using + we set the last bit in the answer to the value that we got in n & 1.
        # 2nd line in the loop we shift bits of our initial number n to the right, since we've already checked the last bit of n, so we just move on to the next bit.
        
        ans = 0
        for i in range(32):  # For every 32 bits
            ans = (ans << 1) + (n & 1)
            n >>= 1
            # print(ans)
        return ans
            
        