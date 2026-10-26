# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        queue = deque([root])
        flag = False

        while queue:
            node = queue.popleft()

            if node is None:
                flag = True
            else:
                if flag:
                    return False

                queue.append(node.left)
                queue.append(node.right)

        return True