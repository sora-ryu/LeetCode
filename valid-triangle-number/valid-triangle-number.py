class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()    # from small to large numbers
        
        for k in range(len(nums)-1, 1, -1):  # The triplet is nums[i]< nums[j]< nums[k]
            i = 0
            j = k - 1
            
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j-i)   # count at once
                    j -= 1
                else:
                    i += 1
                
        return count
        