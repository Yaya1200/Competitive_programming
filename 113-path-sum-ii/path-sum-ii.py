class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        value = []

        def dfs(root):
            if not root:
                return

            value.append(root.val)

            if not root.left and not root.right:
                if sum(value) == targetSum:
                    output.append(value[:])

            dfs(root.left)
            dfs(root.right)

            value.pop()

        dfs(root)
        return output
        