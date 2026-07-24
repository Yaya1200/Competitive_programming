# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        Queue = []
        level = 0
        Queue.append([root, level])
        while Queue:
            if not root:
                return []
            C = Queue[0][1]
            value = []
            level +=1
            while Queue and C == Queue[0][1]: 
                if Queue[0][0].left:
                    Queue.append([Queue[0][0].left, level]) 
                if Queue[0][0].right:
                    Queue.append([Queue[0][0].right, level])
                value.append(Queue[0][0].val)
                Queue.pop(0)
                
            output.append(value)
            value = []
        output1 = []
        while output:
            output1.append(output.pop())    
        return output1
            


        