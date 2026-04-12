class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        def backtrack(arr,start):
            for i in range(start,len(nums)):
                arr.append(nums[i])
                if arr not in ans:
                    ans.append(arr[:])
                backtrack(arr[:],i+1)
                arr.pop()
        
        backtrack([],0)
        return ans