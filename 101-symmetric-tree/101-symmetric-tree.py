# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_subtree = root.left
        right_subtree = root.right
        
        def isMirrored(t1: Optional[TreeNode], t2: Optional[TreeNode]):
            if t1 == None and t2 == None: # Both have no leaves
                return True
            if t2 == None or t1 == None:  # Only one side has leaves
                return False
            if t1.val == t2.val:  # return true only if current level nodes are same and childs are all symmetric.
                return isMirrored(t1.left, t2.right) and isMirrored(t1.right, t2.left)
            
        return isMirrored(left_subtree, right_subtree)
        