# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.values = []
        while root or self.stack:
            while root:
                self.stack.append(root)
                root = root.left

            root = self.stack.pop()
            self.values.append(root.val)

            root = root.right


    def next(self) -> int:
        return self.values.pop(0)
        

    def hasNext(self) -> bool:
        if self.values:
            return True
        else:
            return False
    
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()