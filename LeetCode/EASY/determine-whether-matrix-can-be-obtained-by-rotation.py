class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        Turn = 0
        found = False
        if mat == target:
            return True
        while Turn < 3:
            for i in range(len(mat)):
                for j in range(i,len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
            
            for i in range(len(mat)):
                j = 0
                k = len(mat) - 1
                while j < k:
                    mat[i][j], mat[i][k] = mat[i][k], mat[i][j]
                    j += 1
                    k -= 1
            
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if mat[i][j] != target[i][j]:
                        break
                else:
                    continue
                break
            else:
                return True
            Turn += 1

        return False
