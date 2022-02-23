class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        count = collections.Counter(nums)
        return count.most_common()[0][0]