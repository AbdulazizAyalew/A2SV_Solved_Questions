class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix = 0
        remainder = 0
        Hash_set = {0:1}

        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k

            if remainder in Hash_set:
                count += Hash_set[remainder]
            
            Hash_set[remainder] = Hash_set.get(remainder,0) + 1
        
        return count