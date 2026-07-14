"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def maxDepth1(root):
            result = 0
            if not root:
                return 0
            for i in root.children:
                maxdepth = maxDepth1(i)
                result = max(result, maxdepth)
            return result +1
        return  maxDepth1(root)
       

        