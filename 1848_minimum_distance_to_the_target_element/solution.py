from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = float('inf')
        
        for index, value in enumerate(nums):
            if value == target:
                curr = abs(index - start)
                result = min(curr, result)
            
        return result
