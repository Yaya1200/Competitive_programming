# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countNodes1(root):
            if not root:
                return 0
            return 1+countNodes1(root.left)+countNodes1(root.right)
        return countNodes1(root)
            