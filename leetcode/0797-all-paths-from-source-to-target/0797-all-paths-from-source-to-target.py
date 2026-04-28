class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        paths = []

        def dfs(node, path):
            path.append(node)

            if node == target:
                paths.append(path[:])
            else:
                for neighbor in graph[node]:
                    dfs(neighbor, path)

            path.pop() 

        dfs(0, [])

        return paths