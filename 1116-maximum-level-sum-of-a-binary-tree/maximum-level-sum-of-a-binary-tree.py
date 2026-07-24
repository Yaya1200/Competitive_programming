# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        Queue = []
        Queue.append([root, level])
        value = []
        v = float('-inf')
        k = 0
        while Queue:
            c = Queue[0][1]
            level += 1
            while Queue and c == Queue[0][1]:
                if Queue[0][0].right:
                    Queue.append([Queue[0][0].right, level])
                if Queue[0][0].left:
                    Queue.append([Queue[0][0].left, level])
                value.append(Queue[0][0].val)
                Queue.pop(0)
            if v < sum(value):
                k = level-1
                v = sum(value)
            value = []
        return k
        