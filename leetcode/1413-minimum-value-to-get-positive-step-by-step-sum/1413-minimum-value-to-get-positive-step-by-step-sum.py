class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        startValue = 1
        prefix_arr = []
        summ = startValue

        for i in range(len(nums)):
            summ += nums[i]

            if summ < 1:
                diff = 1 - summ
                startValue += diff
                summ += diff
            
            prefix_arr.append(summ)
        
        return startValue
