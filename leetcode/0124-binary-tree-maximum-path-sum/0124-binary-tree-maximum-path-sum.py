class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_global = float('-inf')

        def get_max_gain(node):
            if not node:
                return 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            current_path_sum = node.val + left_gain + right_gain

            self.max_global = max(self.max_global, current_path_sum)
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return self.max_global