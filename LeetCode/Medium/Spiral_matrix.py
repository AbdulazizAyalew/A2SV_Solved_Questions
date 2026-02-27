class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        ans.append([rStart, cStart])
        
        r, c = rStart, cStart 
        step = 1  
        
        while len(ans) < rows * cols:
            
            for _ in range(step):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
                    if len(ans) == rows * cols:
                        return ans
            
            for _ in range(step):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
                    if len(ans) == rows * cols:
                        return ans
            
            step += 1  
            
            for _ in range(step):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
                    if len(ans) == rows * cols:
                        return ans
            
            for _ in range(step):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
                    if len(ans) == rows * cols:
                        return ans
            
            step += 1  
        
        return ans
