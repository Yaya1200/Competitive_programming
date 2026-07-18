# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def parentNode(root, subRoot):
            if not root:
                return False
            if root.val == subRoot.val:
                if checkNode(root, subRoot):
                    return True
            return parentNode(root.left, subRoot) or parentNode(root.right, subRoot)
        def checkNode(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root:
                return False
            elif not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return checkNode(root.left, subRoot.left) and checkNode(root.right, subRoot.right)
        return  parentNode(root, subRoot)
            

            