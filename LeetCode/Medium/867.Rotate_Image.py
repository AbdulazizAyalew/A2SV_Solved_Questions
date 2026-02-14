class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for j in range(len(matrix)):
            i = 0
            k = len(matrix[0]) - 1
            while i < k:
                matrix[j][i],matrix[j][k] = matrix[j][k], matrix[j][i]
                i += 1
                k -= 1

