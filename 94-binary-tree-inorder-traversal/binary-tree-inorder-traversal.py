# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iot(self,node, result):
        if not node:
            return 
        self.iot(node.left, result)
        result.append(node.val)
        self.iot(node.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.iot(root,result)
        return result

        