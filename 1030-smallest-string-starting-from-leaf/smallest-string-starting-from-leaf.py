# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = [None]

        def dfs(root, array):
            if not root:
                return

            array.append(root.val)

            if not root.left and not root.right:
                path = array[::-1]

                if ans[0] is None or path < ans[0]:
                    ans[0] = path

            dfs(root.left, array)
            dfs(root.right, array)

            array.pop()

        dfs(root, [])

        return ''.join(chr(ord('a') + x) for x in ans[0])