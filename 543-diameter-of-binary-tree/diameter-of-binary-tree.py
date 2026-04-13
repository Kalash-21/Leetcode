# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.maxDiameter = 0
        
        def helper(node):
            # base case?
            if not node :
                return 0
            # get left height
            x=helper(node.left)
            # get right height
            y=helper(node.right)
            # update self.maxDiameter
            self.maxDiameter=max(self.maxDiameter,x+y)
            # return height of current node
            return 1+max(x,y)
        
        helper(root)
        return self.maxDiameter