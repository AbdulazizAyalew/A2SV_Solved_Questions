class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def backtrack(cols,dig_1,dig_2, arr, row):

            if len(arr) == n:
                ans.append(list(arr)) 
                return

            for i in range(n):
                diag1 = row - i
                diag2 = row + i                
                if i in cols or diag1 in dig_1 or diag2 in dig_2:
                    continue
                else:
                    col = cols.copy()
                    col.add(i)
                    d_1 = dig_1.copy()
                    d_1.add(diag1)
                    d_2 = dig_2.copy()
                    d_2.add(diag2)
                    
                    row_str = ["." for _ in range(n)]
                    row_str[i] = "Q"
                    
                    arr.append("".join(row_str))
                    backtrack(col,d_1,d_2, arr, row + 1)
                    arr.pop()
            return
        
        backtrack(set(),set(),set() ,[], 0)
        return ans