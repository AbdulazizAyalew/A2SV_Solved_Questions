

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        incoming = [0 for i in range(numCourses)]
        que = deque()
        result = []

        for course,pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        

        for i in range(len(incoming)):
            if incoming[i] == 0:
                que.append(i)
        
        while que:
            course = que.popleft()
            result.append(course)

            for neigh in graph[course]:
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    que.append(neigh)
        
        if len(result) == numCourses:
            return result
        else:
            return []