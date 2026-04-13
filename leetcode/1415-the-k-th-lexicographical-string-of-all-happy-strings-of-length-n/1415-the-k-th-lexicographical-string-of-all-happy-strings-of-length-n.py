class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        inps = ["a","b","c"]
        def backtrack(arr):
            if len(arr) == n:
                res.append("".join(arr))
                return
            
            for i in range(3):
                if arr and arr[-1] == inps[i]:
                    continue
                arr.append(inps[i])
                backtrack(arr)
                arr.pop()
        
        backtrack([])
        return res[k-1] if len(res) >= k else ""
        