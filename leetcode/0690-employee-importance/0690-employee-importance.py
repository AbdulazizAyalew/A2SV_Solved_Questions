"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        data = {}
        for e in employees:
            data[e.id] = e

        visited = set()
        
        importance = 0
        def dfs(emp):
            visited.add(emp.id)
            nonlocal importance
            importance += emp.importance

            for e in emp.subordinates:
                if e not in visited:
                    dfs(data[e])

        for emp in employees:
            if emp.id == id:
                dfs(emp)    
                return importance


        return importance   