from typing import List
from collections import deque
class Solution:
    def colorGrid(self, n: int, m: int, sources: List[List[int]]) -> list[list[int]]:
        # BFS pattern - Multi Source
        grid = [[0] * m for _ in range(n)]
        queue = deque()
        dist = [[-1] * m for _ in range(n)]     # <- initialize array distance
        
        for r, c, color in sources:     # <- seed sources
            grid[r][c] = color
            dist[r][c] = 0      
            queue.append((r, c, color, 0)) # <- carry distance in queue
            
        directions = [(1, 0),(-1,0),(0,1),(0,-1)]
        dist[r][c] = 0
        while queue:
                r, c, color, d = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    new_dist = d + 1
                    if 0 <= nr < n and 0 <= nc < m:
                        if dist[nr][nc] == -1:      # unvisited
                            dist[nr][nc] = new_dist
                            grid[nr][nc] = color
                            queue.append((nr, nc, color, new_dist))
                        elif dist[nr][nc] == new_dist and grid[nr][nc] < color:     # tie, higher color wins
                            grid[nr][nc] = color
                            queue.append((nr, nc, color, new_dist))
        return grid 
                    
                    
                