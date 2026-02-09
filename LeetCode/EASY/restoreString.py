class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        Result = [" " for i in range(len(s))]

        for j in range(len(s)):
            Result[indices[j]] = s[j]

        return "".join(Result) 
