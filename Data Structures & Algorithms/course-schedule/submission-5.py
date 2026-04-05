from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        # Build graph
        for a, b in prerequisites:
            graph[b].append(a)
        
        # 0 = unvisited, 1 = visiting, 2 = done
        state = [0] * numCourses
        
        def dfs(node):
            if state[node] == 1:
                return False  # cycle detected
            if state[node] == 2:
                return True   # already processed
            
            state[node] = 1  # mark as visiting
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2  # mark as done
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True