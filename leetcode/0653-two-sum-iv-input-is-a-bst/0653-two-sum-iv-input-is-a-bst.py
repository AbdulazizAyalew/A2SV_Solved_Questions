# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        checked = set()
        def find(root,k):
            if not root:
                return False

            if k - root.val in checked:
                return True
            
            if root.val not in checked:
                checked.add(root.val)
            
            return (find(root.left,k) or find(root.right,k))
        
        return find(root,k)

        