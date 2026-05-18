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
        
        total = 0

        emp_hash_map = {emp.id:emp for emp in employees}

        def dfs(employ):

            nonlocal total
            total += employ.importance

            for subordinates in employ.subordinates:
                dfs(emp_hash_map[subordinates])
            
            return total


        return dfs(emp_hash_map[id])
