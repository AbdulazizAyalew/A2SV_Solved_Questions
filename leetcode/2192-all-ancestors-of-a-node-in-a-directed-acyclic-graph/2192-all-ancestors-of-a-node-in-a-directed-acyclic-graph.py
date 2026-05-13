class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        for x,y in edges:
            graph[y].append(x)
        
        
        answer = [[] for i in range(n)]
        queue = deque()  # 1. Initialize once OUTSIDE the loop
        print(graph)
        
        for i in range(n):
            queue.extend(graph[i])  
            checked = set()
            while queue:
                
                num = queue.popleft()
                if num not in checked:
                    answer[i].append(num)
                checked.add(num)
                for x in graph[num]:
                    if x not in checked:
                        queue.append(x)
            
            answer[i].sort()
        
        return answer