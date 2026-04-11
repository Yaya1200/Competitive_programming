class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        curr1 = dummy1
        curr2 = dummy2
        value1 = head

        while value1: 
            Next_Node = value1.next
            if value1.val < x:
                curr1.next = value1
                curr1 = curr1.next   
            else:
                curr2.next = value1
                curr2 = curr2.next 
            value1.next = None  
            value1 = Next_Node

        curr1.next = dummy2.next
        return dummy1.next