class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i, num in enumerate(nums):    # i : index / num : element= nums[i]
            #print(i, num)
            if target - num in nums and nums.index(target-num) != i:
                output.append(i)
                output.append(nums.index(target-num))
                break
        
        return output