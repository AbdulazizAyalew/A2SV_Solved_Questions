class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def check_edge(i,j):
            nonlocal surrounded
            for x,y in directions:
                ni,ny = i+x,j+y
                if ni >= len(board) or ni < 0 or ny >= len(board[0]) or ny < 0:
                    surrounded = False
        def dfs(i,j):
            visited.add((i,j))
            visited_reg.add((i,j))
            check_edge(i,j)
            for x,y in directions:
                ni,ny = i+x, j+y
                if 0 <= ni < len(board) and 0 <= ny < len(board[0]) and (ni,ny) not in visited and board[ni][ny] == "O":
                    dfs(ni,ny)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    surrounded = True
                    visited_reg = set()
                    dfs(i,j)
                    if surrounded:
                        for x,y in visited_reg:
                            board[x][y] = "X"
                                