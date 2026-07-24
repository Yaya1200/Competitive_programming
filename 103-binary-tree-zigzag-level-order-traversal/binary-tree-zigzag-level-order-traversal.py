# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        level = 0
        if not root:
            return []
        Queue = []
        Queue.append([root, level])
        value = []
        v = 1
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
            if v == 0:
                value.reverse()
            v = level%2
            output.append(value)
            value = []
            

        return output

