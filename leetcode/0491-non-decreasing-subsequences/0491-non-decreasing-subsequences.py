class Solution:
    def findSubsequences(self, nums):
        ans = set()
        
        def backtrack(arr, i):
            if i == len(nums):
                if len(arr) >= 2:
                    ans.add(tuple(arr))
                return
            
            if not arr or nums[i] >= arr[-1]:
                arr.append(nums[i])
                backtrack(arr, i+1)
                arr.pop()
            
            backtrack(arr, i+1)
        
        backtrack([], 0)
        return list(ans)