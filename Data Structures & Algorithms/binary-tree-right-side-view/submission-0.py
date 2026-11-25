# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # level order traversal

        queue = collections.deque()
        queue.append(root)
        while queue:
            rightSide = None
            qLen = len(queue) # explore only one level at a time
            for i in range(qLen): # go through every element in that level
                node = queue.popleft() # this loop removes all elements from the current level
                if node:
                    rightSide = node # once whole for executes this will contain the right most ele
                    queue.append(node.left) # always add left before right so that right ele remains at the end 
                    queue.append(node.right)
            if rightSide:        
                result.append(rightSide.val)
        return result




       