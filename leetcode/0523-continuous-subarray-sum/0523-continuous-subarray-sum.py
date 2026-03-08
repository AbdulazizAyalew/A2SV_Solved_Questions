class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_arr = []
        summ = 0
        
        rmndr = {0:0}
        for i in range(len(nums)):
            prefix_arr.append(summ + nums[i])
            summ += nums[i]
            if summ % k not in rmndr:
                rmndr[summ % k] = i + 1
            else:
                if i + 1 - rmndr[summ % k] > 1:
                    return True
        return False


        
        

        

        