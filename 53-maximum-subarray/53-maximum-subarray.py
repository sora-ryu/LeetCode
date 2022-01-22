class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        startSum = 0
        largestSum = nums[0]
        
        for num in nums:
            startSum += num     # First add current number
            if startSum < num:  # Leave old substrings and Refresh
                startSum = num
            largestSum = max(startSum, largestSum)   # Keep tracking for the largest summation
            print(largestSum)
            
        return largestSum
                
#         # Temporally sort the nums array, starting from the biggest element
#         sorted_nums = sorted(nums)[::-1]
#         print(sorted_nums)
        
#         # As the subarray should contain at least one number, add the biggest element
#         cur_index = nums.index(sorted_nums[0])
#         answer = nums[cur_index]
        
#         # As long as the elements are positive and the sum between those elements are also positive, try to add those contiguous subarray.
#         for i in range(1, len(sorted_nums)):
#             next_index = nums.index(sorted_nums[i])
#             if sorted_nums[i] < 0 or len(sorted_nums) == 1:
#                 break
            
#             print(cur_index, next_index)
#             sums = sum(nums[min(cur_index, next_index):max(cur_index, next_index)+1])
#             if sums > answer:
#                 answer = sums
#         ## Cannot handle the duplicated elements!! 

#         return answer
        