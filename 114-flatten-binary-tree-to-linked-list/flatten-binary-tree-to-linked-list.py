# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
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

        dummy = TreeNode()
        curr = dummy

        def dfs(root):
            nonlocal curr
            if not root:
                return

            left = root.left
            right = root.right

            curr.right = root
            curr.left = None
            curr = curr.right

            dfs(left)
            dfs(right)

        dfs(root)
        dummy.right.left = None