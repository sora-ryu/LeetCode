# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Use the information that the binary tree is already sorted!
        
        def search(root) -> int:
            ans = []
            if not root:
                return []
            if root.left:
                ans += search(root.left)
            ans.append(root.val)
            if root.right:
                ans += search(root.right)
            return ans
            
        
        return search(root)[k-1]
        
        