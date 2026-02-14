class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        Result = []
        
        for i in range(len(image)):
            row = []
            for j in range(len(image[0]) - 1,-1, -1):
                row.append(0 if image[i][j] == 1 else 1)
            Result.append(row)

        return Result
                    
