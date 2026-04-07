from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0] # edge case - single node
        
        # Step 1: build adjacency list + degree array
        adj = [[] for _ in range(n)] # list of n empty lists
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a) # undirected - both directiosn
            
        degree = [len(adj[i]) for i in range(n)]
        
        # Step 2: seed queue with all leaves (degree = 1)
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
                
        # Step 3: trim leaves until remaining <= 2
        remaining = n
        while remaining > 2:
            
            leaf_count = len(queue)
            for _ in range(leaf_count):
                
                node = queue.popleft()
                remaining -= 1
                
                for neighbor in adj[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                  
        return list(queue)