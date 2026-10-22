# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not preorder or not postorder:
            return 
        root = TreeNode(preorder[0])
        stack = [root]
        j = 0

        for i in range(1, len(preorder)):
            tree = TreeNode(preorder[i])

            while stack and stack[-1].val == postorder[j]:
                stack.pop()
                j += 1

            if stack[-1].left is None:
                stack[-1].left = tree
            else:
                stack[-1].right = tree

            stack.append(tree)

        return root