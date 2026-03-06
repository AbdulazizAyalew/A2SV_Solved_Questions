# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        second = node.next

        while second.next:
            prev.val = second.val
            prev = prev.next
            second = second.next
            
        prev.val = second.val
        prev.next = None
        
        

        