class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indx = {}

        for i in range(len(nums)):
            if target - nums[i] in nums_indx:
                return [i, nums_indx[target-nums[i]]]
            else:
                nums_indx[nums[i]] = i
