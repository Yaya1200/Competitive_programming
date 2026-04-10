# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        output = []
        value = 0
        while head:
            output.append(head.val)
            head = head.next
        for i in range(len(output)):
            if output[i] == 1:
                value += 2 ** (len(output)-i-1)
        return value
        