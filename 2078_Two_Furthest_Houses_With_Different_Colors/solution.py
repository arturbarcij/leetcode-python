from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance = 1
        max_distance = float('-inf')
        
        for i in range(len(colors)):
            for j in range(1, len(colors)):
                if colors[i] != colors[j]:
                    distance = abs(i - j)
                    if distance > max_distance:
                        max_distance = distance

    
        return max_distance
