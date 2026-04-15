# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        pointer1 = head
        while pointer1:
            count = 1
            pointer2 = pointer1
            while count < k:
                pointer1 = pointer1.next
                count += 1
                if pointer1 == None:
                    curr.next = pointer2
                    return dummy.next
            next_pointer = pointer1.next
            pointer1.next = None
            prev = None
            while pointer2:
                temp = pointer2.next
                pointer2.next = prev
                prev = pointer2
                pointer2 = temp
            curr.next = prev
            while curr.next:
                curr = curr.next
            pointer1 = next_pointer
        return dummy.next
