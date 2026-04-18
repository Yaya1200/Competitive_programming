class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        curr1 = dummy1
        curr2 = dummy2
        while head:
            if head.val < x:
                temp = head.next
                head.next = None
                curr1.next = head
                curr1 = curr1.next
                head = temp
            else:
                temp = head.next
                head.next = None
                curr2.next = head
                curr2 = curr2.next
                head = temp
        curr1.next = dummy2.next
        return dummy1.next

