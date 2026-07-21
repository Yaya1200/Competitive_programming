# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def range(root, low, high):
            if not root:
                return 0

            if root.val < low:
                return range(root.right, low, high)

            if root.val > high:
                return range(root.left, low, high)
            return root.val + range(root.left, low, high) + range(root.right, low, high)
        return range(root, low, high)
      

        