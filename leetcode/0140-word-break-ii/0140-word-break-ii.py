class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def backtrack(arr,start,length):
            if length == len(s):
                res.append(" ".join(arr[:]))
                return
            w = []
            for i in range(start,len(s)):
                w.append(s[i])
                if "".join(w) not in wordDict:
                    continue
                arr.append("".join(w[:]))
                length += len(w)
                backtrack(arr,i+1,length)
                arr.pop()
                length -= len(w)
            
            return
        
        backtrack([],0,0)
        return res
