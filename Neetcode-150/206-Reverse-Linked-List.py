# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myList = []
        cur = head
        while cur:
            myList.append(cur.val)
            cur = cur.next
        cur = head
        index = -1
        while cur:
            cur.val = myList[index]
            index -= 1
            cur = cur.next
        return(head)
