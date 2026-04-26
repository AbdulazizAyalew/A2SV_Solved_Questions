class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacfic = set()


        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,visited):
            visited.add((i,j))
            for x,y in directions:
                ni,ny = i+x,j+y
                if 0 <= ni < len(heights) and 0 <= ny < len(heights[0]) and heights[i][j] <= heights[ni][ny] and (ni,ny) not in visited:
                    dfs(ni,ny,visited)


        #For Pacfic Top and Left call
        for i in range(0,len(heights)):
            dfs(i,0,pacfic)
        for j in range(0, len(heights[0])):
            dfs(0,j,pacfic)
        
        #For atlantic Bottom and Right
        for i in range(len(heights)):
            dfs(i,len(heights[0])-1,atlantic)
        for j in range(len(heights[0])):
            dfs(len(heights)-1,j,atlantic)
        
        return list(atlantic & pacfic)
        

