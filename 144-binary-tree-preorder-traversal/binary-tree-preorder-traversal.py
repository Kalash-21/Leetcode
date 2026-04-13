# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def preOrder(self,node,result):
        if not node :
            return 
        else:
            result.append(node.val)
            self.preOrder(node.left,result)
            self.preOrder(node.right,result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root: return result
        self.preOrder(root,result)
        return result