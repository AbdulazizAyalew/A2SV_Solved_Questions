class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        self.ans = float('inf')
        
        def backtrack(idx):
            if idx == len(cookies):
                self.ans = min(self.ans, max(children))
                return
            
            if max(children) >= self.ans:
                return

            for i in range(k):
                children[i] += cookies[idx]
                backtrack(idx + 1)
                children[i] -= cookies[idx]

                if children[i] == 0:
                    break
                    
        backtrack(0)
        return self.ans