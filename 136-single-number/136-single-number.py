class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # print(list(set(nums)))   # remove duplicates
        for num in nums:
            # print(nums.index(num))
            # print(nums[::-1].index(num))   # there's no rindex function for list.
            
            if nums.index(num) + nums[::-1].index(num) == len(nums) - 1:
                return num
            