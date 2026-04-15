# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def findmax(arr):
            maxx = -999
            indx = -1
            for i in range(len(arr)):
                if arr[i] > maxx:
                    maxx = arr[i]
                    indx = i
            
            return indx


        def buildTree(arr):
            if not arr:
                return

            i = findmax(arr) 
            node = TreeNode(arr[i])
            node.left = buildTree(arr[:i])
            node.right = buildTree(arr[i+1:])

            return node
        
        head = buildTree(nums)
        return head
                  