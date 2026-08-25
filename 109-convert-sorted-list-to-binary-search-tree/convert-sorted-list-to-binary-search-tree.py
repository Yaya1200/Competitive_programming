# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def fill(head):
            if not head:
                return None

            slow = head
            fast = head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            right = slow.next

            if prev:
                prev.next = None

            root = TreeNode(slow.val)

            if prev:
                root.left = fill(head) 
            root.right = fill(right)

            return root

        return fill(head)
