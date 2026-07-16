# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumLeaves(root, flag):
            count = 0
            if not root:
                return 0
            if not root.left and not root.right and flag == 0:
                count += root.val
            return count + sumLeaves(root.left, 0) + sumLeaves(root.right, 1)
        return sumLeaves(root, 1)
        
        
        