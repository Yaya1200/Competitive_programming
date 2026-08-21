# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        while head:
            output.append(head.val)
            head = head.next
        output.sort()
        dummy = ListNode(0)
        curr = dummy
        for i in output:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
            
        