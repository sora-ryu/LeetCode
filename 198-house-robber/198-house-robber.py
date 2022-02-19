class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dynamic programming!
        
        pre, cur = 0, 0   # pre: past, cur: current, num: future
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
            # print(pre, cur)
        
        return cur
        