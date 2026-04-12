# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if  root and not subRoot:
            return False
        if not root and  subRoot:
            return False
        if root.val == subRoot.val:
            return self.isSameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSameTree(self,p, q):
        if not p and not q:
            return True 
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val == q.val:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
            else:
                return False


        