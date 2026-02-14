class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        no_negatives = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    no_negatives += 1

        return no_negatives        
