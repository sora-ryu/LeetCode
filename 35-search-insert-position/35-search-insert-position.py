class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Use that it's already sorted
        left, right = 0, len(nums)-1 
        mid = nums[(right-left)//2]
            
        while left != right-1 and left < right:
            mid = nums[(right+left)//2]
            print(nums[left], nums[right], mid)
            if mid < target:
                left = nums.index(mid) + 1
            elif target < mid:
                right = nums.index(mid) - 1
            else:
                break
            
        # The array will have the length of 2.
        # print(nums[left], nums[right], mid)
        final_array = nums[left:right+1]
        print(final_array)
        
        if target in final_array:
            return final_array.index(target) + left
        elif target < final_array[0]:
            return max(left, 0)
        elif target > final_array[-1]:
            return right + 1
        elif final_array[0] < target and target < final_array[1]:
            return right
        
                
        
        
        
#         # Runtime : O(n)
#         for i in range(len(nums)-1):
#             if target == nums[i]:   # If the target is in nums array
#                 return i
#             elif nums[i] < target and target < nums[i+1]:   # If its value is within the range
#                 return i+1
#             elif target > nums[len(nums)-1]:   # If it's too large
#                 return len(nums)
#             elif target < nums[0]:   # If it's too small
#                 return 0
            
#         # return nums.index(target)
        