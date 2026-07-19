# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash_map = {}
        count = 0
        count1 = []
        def find(root):
            if not root:
                return 
            if root.val not in hash_map:
                hash_map[root.val] = 1
            else:
                hash_map[root.val] += 1
            find(root.left)
            find(root.right)
        find(root)
        for i in hash_map:
           if count < hash_map[i]:
                count = hash_map[i]
        for i in hash_map:
            if hash_map[i] == count:
                count1.append(i)
        return count1
       

       
        
        