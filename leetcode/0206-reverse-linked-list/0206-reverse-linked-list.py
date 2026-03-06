# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head.next
            first = True
            while curr:
                if first:
                    first = False
                    head.next = None
                temp = curr.next
                curr.next = head
                head = curr
                curr = temp
                
            return head
        else:
            return