# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Time Complexity: O(N^2)
        # The worst case is when the nums array is sorted (ascending order)
        # it takes O(N * N) while N is for finding maximum value, and
        # another N is for constructing subtree for each level
        if nums:
            max_idx, max_val = max(enumerate(nums), key=lambda x: x[1])
            node = TreeNode(max_val)
            node.left = self.constructMaximumBinaryTree(nums[:max_idx])
            node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
            return node