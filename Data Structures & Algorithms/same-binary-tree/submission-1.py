# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #base case
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        # call same funtion on left and right node
        leftSideResult = self.isSameTree(p.left,q.left)
        rightSideResult = self.isSameTree(p.right,q.right)

        return p.val == q.val and leftSideResult and rightSideResult

        
        
        

        