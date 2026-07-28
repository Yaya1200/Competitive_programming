# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_root = root.left
        right_root = root.right
        def dfs(left_root, right_root):
            if not left_root and not right_root:
                return True
            if not left_root or not right_root:
                return False
            if left_root.val != right_root.val:
                return False
            return dfs(left_root.left,right_root.right) and dfs(left_root.right, right_root.left) 
        return dfs(left_root, right_root)
            
        