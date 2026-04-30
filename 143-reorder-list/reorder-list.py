# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        temp = head
        while temp:
            temp1 = temp.next
            temp.next = None
            stack.append(temp)
            temp = temp1
        left = 0
        right = len(stack)-1
        head = ListNode(0)
        curr = head
        while left < right:
            stack[left].next = stack[right]
            left += 1
            if left == right:
                break
            stack[right].next = stack[left]
            right -= 1
        stack[left].next = None

        
            
