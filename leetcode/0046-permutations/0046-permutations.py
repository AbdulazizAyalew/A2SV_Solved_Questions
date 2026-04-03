class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False] * len(nums)

        def backtracker(perm):
            if len(perm) == len(nums):
                ans.append(perm[:])
                return

            for j in range(0,len(nums)):
                if visited[j]:
                    continue
                perm.append(nums[j])
                visited[j] = True

                backtracker(perm)

                perm.pop()
                visited[j] = False
        

        backtracker([])
        return ans