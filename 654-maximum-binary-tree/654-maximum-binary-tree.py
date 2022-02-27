# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if nums:
            max_idx, max_val = max(enumerate(nums), key=lambda x: x[1])
            node = TreeNode(max_val)
            node.left = self.constructMaximumBinaryTree(nums[:max_idx])
            node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
            return node