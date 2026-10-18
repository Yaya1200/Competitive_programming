# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = right
        self.flatten(left)
        self.flatten(right)
        