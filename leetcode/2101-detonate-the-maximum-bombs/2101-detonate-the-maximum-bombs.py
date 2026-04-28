class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = []
        for i in range(len(bombs)):
            x,y,z = bombs[i]
            graph.append([])
            for j in range(len(bombs)):
                if i != j:
                    distance = (x-bombs[j][0]) ** 2 + (y-bombs[j][1]) ** 2
                    if z**2 >= distance:
                        graph[i].append(j)

        def dfs(i,visited):
            visited.add(i)
            for n in graph[i]:
                if n not in visited:
                    dfs(n,visited)

        maxx = 0

        for i in range(len(bombs)):
            visited = set()
            dfs(i,visited)

            maxx = max(maxx,len(visited))
        
        return maxx