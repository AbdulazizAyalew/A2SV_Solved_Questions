class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def count_ones(i,j):
            count = 0
            for x,y in directions:
                ni,ny = i+x,j+y
                if 0 <= ni < len(grid) and 0 <= ny < len(grid[0]) and grid[i+x][j+y] == 1:
                    count += 1
            return count 
        
        def dfs(i,j):
            nonlocal perimeter
            visited.add((i,j))
            if grid[i][j] == 1:
                count = count_ones(i,j)
                perimeter += (4-count)

            for x,y in directions:
                ni,ny = i+x,j+y
                if 0 <= ni < len(grid) and 0 <= ny < len(grid[0])  and (i+x,j+y) not in visited and grid[ni][ny] == 1:
                    dfs(ni,ny)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return perimeter
        
                
                
