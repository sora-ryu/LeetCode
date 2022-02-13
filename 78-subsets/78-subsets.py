class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Input: [1,2,3]
        # [[], [1]]
        # [[], [1], [2], [1, 2]]
        # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        
        ans = [[]]
        for num in nums:
            ans += [i + [num] for i in ans]
            print(ans)
        
        return ans
        