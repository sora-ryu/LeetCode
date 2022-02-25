# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Diameter = the sum of the depth of left subtree and the depth of right subtree
        # or the sums of left subtrees or right subtrees (This path may not pass through the root.)
        pathlen = 0
        def helper(node):
            if not node:
                return 0
            nonlocal pathlen
            left = helper(node.left)
            right = helper(node.right)
            pathlen = max(pathlen,left+right)
            return 1+max(left,right)
        
        helper(root)
        return pathlen