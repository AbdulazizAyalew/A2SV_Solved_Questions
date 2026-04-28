class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        

        def checkInside(d,b):
            distance = sqrt((d[0]-b[0]) ** 2 + (d[1]-b[1]) ** 2)
            if 0 <= distance <= d[2]:
                return True

        

        def dfs(b,checked,i):
            checked[i] = 1
            for i in range(len(bombs)):
                if checkInside(b,bombs[i]) and checked[i] != 1:
                    dfs(bombs[i],checked,i)

        maxx = 0

        for i in range(len(bombs)):
            checked = [0 for i in range(len(bombs))]
            dfs(bombs[i],checked,i)

            maxx = max(maxx,checked.count(1))
        
        return maxx