# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        queue = deque([(root, 0)])
        max_length = 0

        while queue:
            level_size = len(queue)
            first = queue[0][1]
            last = first

            for i in range(level_size):
                node, index = queue.popleft()

            
                index -= first
                last = index

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))

            max_length = max(max_length, last + 1)

        return max_length