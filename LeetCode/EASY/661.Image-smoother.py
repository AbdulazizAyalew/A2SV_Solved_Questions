class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        changes = []
        for i in range(len(img)):
            for j in range(len(img[0])):
                s = img[i][j]
                tot = 1
                # top
                if i-1 >= 0:
                    s += img[i-1][j]
                    tot += 1
                # top left
                if i-1 >= 0 and j-1 >= 0:
                    s += img[i-1][j-1]
                    tot += 1
                # top right
                if i-1 >= 0 and j+1 < len(img[0]):
                    s += img[i-1][j+1]
                    tot += 1
                # mid left
                if j-1 >= 0:
                    s += img[i][j-1]
                    tot += 1
                # mid right
                if j+1 < len(img[0]):
                    s += img[i][j+1]
                    tot += 1
                # bottom
                if i+1 < len(img):
                    s += img[i+1][j]
                    tot += 1
                # bottom left
                if i+1 < len(img) and j-1 >= 0:
                    s += img[i+1][j-1]
                    tot += 1
                # bottom right
                if i+1 < len(img) and j+1 < len(img[0]):
                    s += img[i+1][j+1]
                    tot += 1
                
                ave = s//tot
                changes.append([i, j, ave])
        for c in changes:
            img[c[0]][c[1]] = c[2]
        return img 
