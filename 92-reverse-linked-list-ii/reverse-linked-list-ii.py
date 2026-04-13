# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = 1
        r = left

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        dummy3 = ListNode(0)

        curr1 = dummy1
        curr2 = dummy2
        curr3 = dummy3

        while head:
            if l < left:
                curr1.next = head
                curr1 = curr1.next
                l += 1
            elif r <= right:
                curr2.next = head
                curr2 = curr2.next
                r += 1
            else:
                curr3.next = head
                curr3 = curr3.next

            head = head.next  

  
        curr1.next = None
        curr2.next = None
        curr3.next = None
        
        prev = None
        value1 = dummy2.next
        while value1:
            temp = value1.next
            value1.next = prev
            prev = value1
            value1 = temp
        curr1.next = prev
        while prev and prev.next:
            prev = prev.next
        prev.next = dummy3.next
        return dummy1.next


                