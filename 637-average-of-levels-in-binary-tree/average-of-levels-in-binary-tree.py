# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []
        Queue = []
        Queue.append([root,0])
        value = []
        level = 0
        while Queue:
            level += 1
            C = Queue[0][1]
            while Queue and  C == Queue[0][1]:
                if Queue[0][0].left:
                    Queue.append([Queue[0][0].left, level])
                if Queue[0][0].right:
                    Queue.append([Queue[0][0].right, level]) 
                value.append(Queue[0][0].val)
                Queue.pop(0)
            k = len(value)
            output.append((sum(value)/k))
            value = []
        return output
              
            


        