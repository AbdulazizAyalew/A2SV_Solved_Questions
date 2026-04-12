class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        vals = {"2":['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        given = [vals[d] for d in digits]
        ans = []

        n = len(digits)
        def backtrack(arr,start):
            if len(arr) == n:
                ans.append("".join(arr))
                return
            
            for i in range(len(given[start])):
                arr.append(given[start][i])
                backtrack(arr,start+1)
                arr.pop()
        
        backtrack([],0)
        return ans