# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        head = None
        i, j = list1, list2
        while (i is not None and j is not None):
            if i.val <= j.val:
                result = ListNode(i.val)
                i = i.next
            else:
                result = ListNode(j.val)
                j = j.next
            
            if prev is not None:
                prev.next = result
                prev = result
            else:
                head = prev = result

        while (i is not None and j is None):
            result = ListNode(i.val)

            if prev is not None:
                prev.next = result
                prev = result
            else:
                head = prev = result
            i = i.next

        while (i is None and j is not None):
            result = ListNode(j.val)

            if prev is not None:
                prev.next = result
                prev = result
            else:
                head = prev = result
            j = j.next
        
        return head