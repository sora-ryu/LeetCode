class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Delete last element and append it to the first element
        # => Rotate 1 step to the right
        
        # nums = [1,1,1,3,2]
        # k = 3
        for i in range(k):
            tmp = nums[-1]
            nums.pop()
            nums.insert(0, tmp)
            # print(nums)