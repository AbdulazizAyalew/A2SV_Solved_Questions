class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = 0
        r = 0
        dictt = {}
        count = 0

        plus_1 = 0
        count = 0
        nums_dict = {}
        l = 0
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
            
            while len(nums_dict) > k:
                nums_dict[nums[l]] -= 1
                if nums_dict[nums[l]] == 0:
                    del nums_dict[nums[l]]
                l += 1
            
            if len(nums_dict) <= k:
                plus_1 += (i-l+1)
        
        minus_count = 0
        le = 0
        nums_dict = {}
        for j in range(len(nums)):
            if nums[j] not in nums_dict:
                nums_dict[nums[j]] = 1
            else:
                nums_dict[nums[j]] += 1
            
            while len(nums_dict) > k-1:
                nums_dict[nums[le]] -= 1
                if nums_dict[nums[le]] == 0:
                    del nums_dict[nums[le]]
                
                le += 1
            
            if len(nums_dict) <= k-1:
                minus_count += (j-le+1)

        return plus_1 - minus_count
        
        
        return count
                
