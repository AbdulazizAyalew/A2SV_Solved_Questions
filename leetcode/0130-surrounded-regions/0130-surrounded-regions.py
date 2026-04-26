class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j):
            board[i][j] = "T"
            for x,y in directions:
                ni,ny = i + x, j + y
                if 0 <= ni < len(board) and 0 <= ny < len(board[0]) and board[ni][ny] != "T" and board[ni][ny] == "O":
                    dfs(ni,ny)
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board) -1 or j == 0 or j == len(board[0]) - 1) and ( board[i][j] == "O" and board[i][j] != "T"):
                    dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                else:
                    continue