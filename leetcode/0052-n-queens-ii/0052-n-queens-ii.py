class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []
        cols = set()
        dig_1 = set()
        dig_2 = set()

        def backtrack(arr, row):

            if len(arr) == n:
                ans.append(list(arr)) 
                return

            for i in range(n):
                diag1 = row - i
                diag2 = row + i                
                if i in cols or diag1 in dig_1 or diag2 in dig_2:
                    continue
                else:
                    cols.add(i)
                    dig_1.add(diag1)
                    dig_2.add(diag2)
                    
                    row_str = ["." for _ in range(n)]
                    row_str[i] = "Q"
                    
                    arr.append("".join(row_str))
                    backtrack(arr, row + 1)
                    arr.pop()
                    cols.remove(i)
                    dig_1.remove(diag1)
                    dig_2.remove(diag2)
            return
        
        backtrack([], 0)
        return len(ans)