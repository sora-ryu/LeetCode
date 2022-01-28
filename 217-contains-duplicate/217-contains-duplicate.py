class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for i in nums:
            if not i in dict_nums:
                dict_nums[i] = 1
            else:
                dict_nums[i] += 1
        
        for value in dict_nums.values():
            if value > 1:
                return True
        
        return False