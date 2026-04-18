# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy1 = ListNode(0)
        curr = dummy1
        value = head
        while value and value.next:
            value2 = value.next
            value3 = value2.next
            curr.next = value2
            value2.next = value
            value.next = value3
            curr = value
            value = value3
        return dummy1.next

