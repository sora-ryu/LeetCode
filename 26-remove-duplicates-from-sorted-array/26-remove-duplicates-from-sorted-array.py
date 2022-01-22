class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count, i, prev = 0, 0, nums[0]
        
        while i < len(nums):
            if nums[i] == prev and i != 0:
                nums.remove(nums[i])
            else:
                count += 1
                prev = nums[i]
                i += 1
            # print(count, nums)
        
        return count