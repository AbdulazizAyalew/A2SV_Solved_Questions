class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        Target = targetSum
        count = 0

        def checkSum(root, summ, prefix):
            nonlocal count
            if not root:
                return

            prefix = prefix.copy()

            summ += root.val

            check = summ - Target
            count += prefix.get(check, 0)

            prefix[summ] = prefix.get(summ, 0) + 1

            checkSum(root.left, summ, prefix)
            checkSum(root.right, summ, prefix)

        checkSum(root, 0, {0: 1})
        return count