class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepth1(root):
            if not root:
                return 0
            return 1 + max(maxDepth1(root.left), maxDepth1(root.right))

        return maxDepth1(root)
        