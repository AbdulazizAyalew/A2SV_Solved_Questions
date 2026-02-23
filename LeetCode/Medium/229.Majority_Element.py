class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minn = min(nums)
        maxx = max(nums)

        R = maxx - minn + 1
        new_arr = [0] * R

        for num in nums:
            new_arr[num-minn] += 1
        
        Result = []
        check = len(nums) // 3
        unique_nums = set(nums)
        for n in unique_nums:
            if new_arr[n-minn] > check:
                Result.append(n)
        
        return Result
            
