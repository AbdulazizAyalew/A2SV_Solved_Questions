class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        
        def traverse(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            left_bst, left_min, left_max, left_sum = traverse(node.left)
            right_bst, right_min, right_max, right_sum = traverse(node.right)
            
            if left_bst and right_bst and left_max < node.val < right_min:
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)
                
                return (True, 
                        min(node.val, left_min), 
                        max(node.val, right_max), 
                        current_sum)
            
            return False, 0, 0, 0

        traverse(root)
        return self.max_sum