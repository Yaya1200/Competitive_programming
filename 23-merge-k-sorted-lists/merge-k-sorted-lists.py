# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        length = 0
        j = 0
        temp1 = None
        if not lists or all(l is None for l in lists):
            return None
        while length < len(lists):
            node1 = ListNode(float('inf'))
            for i in range(len(lists)):
                    if lists[i] and node1.val > lists[i].val:
                        temp1 = lists[i].next
                        node1 = lists[i]
                        j = i
            node1.next = None
            curr.next = node1
            curr = curr.next
            lists[j] = temp1
            length = sum(1 for l in lists if l is None)

 
        return dummy.next
        
        