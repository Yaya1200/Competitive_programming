"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        def findchild(root):
            if root and root.children:
                for i in root.children:
                    if not i.children:
                        output.append(i.val)
                    else:
                      findchild(i)
            if root:
              output.append(root.val)
            return output
        return findchild(root)
                    
