# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        root_index = inorder.index(root.val)

        left_size = root_index

        left_preorder = preorder[1:1 + left_size]
        right_preorder = preorder[1 + left_size:]

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root



        