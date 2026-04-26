class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        count_lands = 0
        visited = set()

        def dfs(i,j):
            visited.add((i,j))
            for x,y in directions:
                ni,ny = i+x,j+y 
                if 0 <= ni < len(grid) and 0 <= ny < len(grid[0]) and grid[ni][ny] == "1" and (ni,ny) not in visited:
                    dfs(ni,ny)  
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count_lands += 1
        
        return count_lands

