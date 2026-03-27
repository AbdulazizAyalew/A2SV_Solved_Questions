class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracker(start,lis):
            if len(lis) == k:
                ans.append(lis)
                return
            for j in range(start,n+1):
                lis.append(j)
                backtracker(j+1,lis[:])
                lis.pop()
        

        backtracker(1,[])
        return ans