# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalanced(root):
            if not root:
              return 0
            if not root.left and not root.right:
              return 1
            left_height = isBalanced(root.left)
            right_height = isBalanced(root.right)
            if left_height == -1:
                return -1
            if right_height == -1:
                return -1
            if abs(left_height - right_height) <= 1:
                return 1+ max(left_height, right_height)
            else:
                return -1
        return isBalanced(root) != -1
            
           

