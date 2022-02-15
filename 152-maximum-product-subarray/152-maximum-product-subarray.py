class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_product, max_product, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            # update values [positive consecutive product / negative consecutive product / start new]
            max_product, min_product = max(max_product*nums[i], min_product*nums[i], nums[i]), min(max_product*nums[i], min_product*nums[i], nums[i])
            ans = max(ans, max_product)
            print(max_product, min_product, ans)
        
        return ans
        