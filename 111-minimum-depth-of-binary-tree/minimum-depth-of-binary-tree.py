# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def minDepth1(root):    
            if not root:
                return 0
            if not root.left and not root.right:
               return  1
            left = minDepth1(root.left)
            right = minDepth1(root.right)
            if not left:
                return   right + 1
                
            elif not right:
                return left + 1
            else:
              return 1 + min(left, right)
                 
        return minDepth1(root)
           