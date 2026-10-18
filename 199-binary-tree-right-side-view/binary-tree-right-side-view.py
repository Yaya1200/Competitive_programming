# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append([root])
        output = []

        while queue:
            root_value = queue.popleft()
            output.append(root_value[-1].val)

            result = []
            for i in root_value:
                if i.left:
                    result.append(i.left)
                if i.right:
                    result.append(i.right)

            if result:
                queue.append(result)

        return output