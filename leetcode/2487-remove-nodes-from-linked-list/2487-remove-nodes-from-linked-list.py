# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        start = head

        while start:
            if stack:
                while stack and stack[-1].val < start.val:
                    print(stack[-1].val)
                    temp = stack.pop()
                    temp.next = None
                if stack:
                    stack[-1].next = start
                stack.append(start)
            else:
                stack.append(start)
            
            start = start.next
        
        return stack[0]