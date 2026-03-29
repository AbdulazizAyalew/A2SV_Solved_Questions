# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def calcsum(root,prt,paps):
            nonlocal summ
            if root:
                mine = False
                if paps:
                    summ += root.val
                if root.val % 2 == 0:
                    mine = True
                
                calcsum(root.left,mine,prt)
                calcsum(root.right,mine,prt)
        
        calcsum(root,False,False)
        return summ
                


                
            
        