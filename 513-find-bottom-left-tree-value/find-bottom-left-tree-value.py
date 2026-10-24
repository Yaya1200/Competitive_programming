# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        queue = deque()
        queue.append([root])
        while queue:
            value = queue.popleft()
            nodes = []
            for i in value:
                if i.left:
                    nodes.append(i.left)
                if i.right:
                    nodes.append(i.right)
            if not nodes:
                return value[0].val
            else:
                queue.append(nodes)

        