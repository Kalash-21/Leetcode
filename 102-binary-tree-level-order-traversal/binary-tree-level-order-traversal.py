# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        results1=[]
        while q:
            result=[]
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)    
                result.append(node.val)
            results1.append(result) 
        return results1
            

            
        