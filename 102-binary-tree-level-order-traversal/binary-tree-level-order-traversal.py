# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Queue = []
        output = []
        Queue.append([root, 0])
        level = 0
        while Queue:
            level += 1
            if not root:
                 return []
            C = Queue[0][1]
            value = []
            while Queue and  C == Queue[0][1]:   
                value.append(Queue[0][0].val)
                if Queue[0][0].left:
                    Queue.append([Queue[0][0].left, level])
                if Queue[0][0].right:
                    Queue.append([Queue[0][0].right, level])
                Queue.pop(0)
            output.append(value)
            value = []
        return output    
       
        



        