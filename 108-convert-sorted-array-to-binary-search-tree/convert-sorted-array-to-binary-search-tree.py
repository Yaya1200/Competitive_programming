# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fill(nums,left, right):
                if left > right:
                    return 
                mid = left + (right-left)//2
                dummy = TreeNode(nums[mid])
                dummy.left = fill(nums, left, mid-1)
                dummy.right = fill(nums, mid+1, right)
                return dummy
        return fill(nums,0, len(nums)-1)
        

      