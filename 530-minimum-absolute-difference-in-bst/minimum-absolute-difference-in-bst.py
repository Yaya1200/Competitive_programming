# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def getMin(root):
            if not root:
                return
            values.append(root.val)
            getMin(root.left)
            getMin(root.right)
        getMin(root)
        values = sorted(values)
        minResult = float('inf')
        for i in range(len(values)-1):
            minResult = min(abs(values[i]-values[i+1]),minResult)
        return minResult

        