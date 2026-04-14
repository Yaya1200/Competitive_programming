# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        curr = dummy
        temp1 = head
        while temp1 and temp1.next:
            temp2 = temp1.next
            next_pair = temp1.next.next
            curr.next = temp2
            curr = curr.next
            curr.next = temp1
            curr = curr.next
            temp1 = next_pair
        curr.next = temp1
            
        return dummy.next
