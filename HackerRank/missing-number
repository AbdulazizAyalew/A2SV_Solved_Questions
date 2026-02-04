class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        num_set = set(nums)
        
        for i in range(n):
            if i not in num_set:
                return i
