class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = ["." for i in range(len(graph))]
        visited = [0 for i in range(len(graph))]

        def dfs(node):
            check = True
            if colored[node] == ".":
                colored[node] = "R"
            visited[node] = 1
            for neigh in graph[node]:
                if colored[node] != colored[neigh]:
                    if colored[neigh] == ".":
                        colored[neigh] = "G" if colored[node] == "R" else "R"
                    if visited[neigh] != 1:
                        check = dfs(neigh)
                else:
                    return False
            return check
        Flag = True

        for i in range(len(graph)):
            if visited[i] != 1:
                Flag = Flag and dfs(i)

        return Flag