class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
            return [-1, -1]
        
        return [nums.index(target), len(nums)-1 - nums[::-1].index(target)]