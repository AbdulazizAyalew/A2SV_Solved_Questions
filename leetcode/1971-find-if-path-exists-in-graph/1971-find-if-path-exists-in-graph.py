class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for e_1,e_2 in edges:
            graph[e_1].append(e_2)
            graph[e_2].append(e_1)
        
        visited = [0 for i in range(n)]
        
        def dfs(node):
            nonlocal visited
            if node == destination:
                return True
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] != 1:
                    result = dfs(neighbor)
                    if result:
                        return True
            return False

        return dfs(source)

        
            

        