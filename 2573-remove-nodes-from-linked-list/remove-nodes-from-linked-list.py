# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(0)
        curr = dummy
        while head:
            if not stack:
                stack.append(head.val)
            else:
                while stack and stack[-1] < head.val:
                    stack.pop()
                stack.append(head.val)
            head = head.next
        for i in stack:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        