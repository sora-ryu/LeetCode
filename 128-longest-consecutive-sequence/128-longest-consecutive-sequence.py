class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        max_length, ans = 0, 1    
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                ans += 1
            elif nums[i+1] == nums[i]:
                continue
            else:           
                print(max_length, ans)
                max_length = max(max_length, ans)
                ans = 1
            print(ans)
        
        return max(max_length, ans)
        