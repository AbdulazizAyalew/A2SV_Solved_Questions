# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(left,right):
            Head = ListNode()
            curr = Head

            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                
                curr = curr.next
            if left:
                curr.next = left
            if right:
                curr.next = right
            return Head.next
        
        def merge(node):
            if not node or not node.next:
                return node
            
            start = node
            fast = node
            while fast and fast.next and fast.next.next:
                start = start.next
                fast = fast.next.next
            
            mid = start.next
            start.next = None
            left = merge(node)
            right = merge(mid)

            return mergeSort(left,right)
        
        return merge(head)
        