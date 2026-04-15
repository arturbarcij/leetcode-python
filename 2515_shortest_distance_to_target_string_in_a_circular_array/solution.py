from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return - 1
        
        left_distance = 0
        right_distance = 0
        min_distance = float('inf')
        n = len(words)
    
        for i in range(0, n):
            if words[i] == target:
                left_distance = abs(i - startIndex)
                right_distance = n - left_distance
            
            
                min_distance = min(left_distance, right_distance, min_distance)

        return min_distance
                    