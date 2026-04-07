from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0]) #sort intervals by start time
        
        current = intervals[0]
        result = []
        
        for interval in intervals[1:]:
            if current[1] >= interval[0]: #condition
                current = [current[0], max(current[1], interval[1])]
            else:
                result.append(current)
                current = interval
        
        result.append(current) # last one
        return result
        