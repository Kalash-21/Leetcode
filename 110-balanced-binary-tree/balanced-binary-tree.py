# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,node):
        if not node:
            return True, 0
    
    # get left balanced + height
        else:
            isbalanced_L,height_left=self.helper(node.left)
    # get right balanced + height
            isbalanced_R,height_right=self.helper(node.right)
    # check if current node is balanced
            isbalanced = isbalanced_L and isbalanced_R and abs(height_left - height_right) <= 1
    # return isBalanced, height
            return isbalanced, 1+max(height_left,height_right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x,y=self.helper(root)
        return x
    
        
        