# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp2 = head
        temp1 = head
        count = 0
        result = []
        while temp1:
            count += 1
            temp1 = temp1.next
        num1 = count//k  
        num2 = count % k 
        value = [num1]*k
        for i in range(num2):
            value[i] += 1
        i = 0
        count1 = 1
        curr = temp2
        while temp2:
            if count1 == value[i]:
                temp3 = temp2.next
                temp2.next = None
                result.append(curr)
                temp2 = temp3
                curr = temp2
                count1 = 1
                i+= 1
            else:
                temp2 = temp2.next
                count1 += 1
        while i < len(value):
            result.append(temp2)
            i+=1

        return result



        