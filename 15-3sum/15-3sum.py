class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outer_list = []
        reversed_nums = nums[::-1]  # needed for checking duplicated element index
        
        if len(nums) < 3:
            return outer_list
        
        # Time Limit Exceeded
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 value = 0 - nums[i] - nums[j]
                   
#                 if value in nums and len(nums)-1 - j > reversed_nums.index(value):
#                     # the indices should be index of j < index of value
#                     inner_list = sorted([nums[i], nums[j], value])
#                     if not inner_list in outer_list:
#                         outer_list.append(inner_list)
        
        nums.sort()
        
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:    # duplicated fixed i => already scanned
                continue
            
            left, right = i+1, len(nums)-1 # both larger than i, but the minimum and maximum elements
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums == 0:
                    inner_list = [nums[i], nums[left], nums[right]]
                    if not inner_list in outer_list:
                        outer_list.append(inner_list)
                    left += 1
                    right -= 1
                    
                elif sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
        
        
        return outer_list
        