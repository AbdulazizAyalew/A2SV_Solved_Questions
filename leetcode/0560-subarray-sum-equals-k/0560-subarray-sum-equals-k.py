class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_arr = [0]

        for i in range(len(nums)):
            prefix_arr.append(nums[i]+prefix_arr[i])

        
        ans = {}
        count = 0
        for i in range(len(prefix_arr)):
            if prefix_arr[i] - k in ans:
                count += ans[prefix_arr[i] - k]
            
            if prefix_arr[i] not in ans:
                ans[prefix_arr[i]] = 1
            else:
                ans[prefix_arr[i]] += 1
        
        
        
        return count