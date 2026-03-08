class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -99999999999999
        summ = 0

        for n in nums:
            if summ >= 0:
                summ += n
            else:    
                summ = n
            
            largest_sum = max(summ,largest_sum)
        
        return largest_sum
                




        
        