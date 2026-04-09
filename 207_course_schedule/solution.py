from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: build adjacency list and in-degree count
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1

        # Step 2: seed queue with courses that have no prerequisites
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # Step 3: process queue (Kahn's algorithm)
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
