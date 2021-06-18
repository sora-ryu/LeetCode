# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    1. Through dfs algorithm, find the deepest leaves.
    2. Return the sum of those values.
    '''

        
    def deepestLeavesSum(self, root: TreeNode) -> int:
                
        self.answer = 0
        self.max_level = 0
        
        def dfs(root: TreeNode, level: int):
            if root is None:
                return 0
            if (root.left is None) and (root.right is None):   # it refers to leave node
                if level > self.max_level:      # if there's deeper node, then ignore previous summation process and replace it into current node
                    self.max_level = level
                    self.answer = root.val
                elif level == self.max_level:   # the case of same depth node
                    self.answer += root.val
                    
            level += 1
            
            dfs(root.left, level)
            dfs(root.right, level)
            
        dfs(root, 0)
        
        return self.answer