# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #BASE CASE
        if root is None:
            return None

        #CALLING SAME FUNTION ON LEFT SUBTREE
        self.invertTree(root.left)

        #CALLING THE SAME FUNTION ON THE RIGHT SUB TREE
        self.invertTree(root.right)

        # JOINING RESULT PART
        root.left,root.right = root.right, root.left
        
        return root
    