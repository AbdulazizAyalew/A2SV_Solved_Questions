class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracker(visited,lis):
            if len(lis) == len(nums):
                ans.append(lis)
                return

            for j in range(0,len(nums)):
                if j in visited:
                    continue
                lis.append(nums[j])
                visited.append(j)
                backtracker(visited[:],lis[:])
                lis.pop()
                visited.pop()
        

        backtracker([],[])
        return ans