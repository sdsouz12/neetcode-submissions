# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0 # keeps track of diameter
        
        # this returns max heighr
        def dfs(curr):
            if not curr:
                return 0 # null node height 0
            left = dfs(curr.left) # height for left
            right = dfs(curr.right)# height for right
            # both increase it by one while exploring the tree

            self.result = max(self.result, left + right) # left+ right current diameter 
            return 1 + max( left, right ) # max height will be either from left and right plus one for the current node 

        dfs(root)
        return self.result