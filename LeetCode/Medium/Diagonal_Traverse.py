class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mapper = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mapper[i+j].append((i, j))
        
        res = []
        for s in mapper:
            if s%2 == 0:
                mapper[s].reverse()
            for i, j in mapper[s]:
                res.append(mat[i][j])
        return res
