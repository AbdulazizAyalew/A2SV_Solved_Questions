class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefixes = {0:1}
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - goal in prefixes:
                count += prefixes[summ-goal]

            if summ in prefixes:
                prefixes[summ] += 1
            else:
                prefixes[summ] = 1
                        
        return count

