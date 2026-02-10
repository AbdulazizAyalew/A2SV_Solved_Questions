class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_n = len(nums) // 3
        Freq_nums = Counter(nums)
        Result = []

        for num in Freq_nums:
            if Freq_nums[num] > max_n:
                Result.append(num)
        
        return Result


