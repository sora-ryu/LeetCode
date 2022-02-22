# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def getHeight(root, count):
            if root:
                return max(getHeight(root.left, count+1), getHeight(root.right, count+1))
            return count
        
        def insertElement(root, ans, left, right, depth):
            if not root:
                return None
            middle = (left+right)//2
            ans[depth][middle] = str(root.val)
            insertElement(root.left, ans, left, middle-1, depth+1)
            insertElement(root.right, ans, middle+1, right, depth+1)
            
            return ans
            
            
        height = getHeight(root, 0)
        print(height)
        width = 2 ** height - 1
        ans = [[""] * width for i in range(height)]
        print(ans)
        
        return insertElement(root, ans, 0, width, 0)
        
        