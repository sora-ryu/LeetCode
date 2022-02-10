class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        x = Counter(nums)
        print(x)
        
        return [i for i in range(1, len(nums)+1) if x[i] == 0]
        
#         # TimeLimitExceeded
#         ans = []
#         for i in range(1, len(nums)+1):
#             if not i in nums:
#                 ans.append(i)
        
#         return ans