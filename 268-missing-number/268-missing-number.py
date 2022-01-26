class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        print(len(set(nums)))
        for i in range(len(set(nums))+1):
            if i not in nums:
                return i
        