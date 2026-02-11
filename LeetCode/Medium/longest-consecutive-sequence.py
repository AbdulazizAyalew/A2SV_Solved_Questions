class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_num = sorted(nums)

        max_n = 0
        nn = 1
        for i in range(len(nums)):
            if i < len(nums) - 1 and sorted_num[i+1] == sorted_num[i] + 1:
                nn += 1
            elif i < len(nums) - 1 and sorted_num[i] == sorted_num[i+1]:
                continue
            else:
                max_n = max(max_n,nn)
                nn = 1

        return max_n  

      
