from typing import List
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        values = dict()
        result = []
        
        index_map = {}
        for idx, val in enumerate(nums):
            if val not in index_map:
                index_map[val] = []
            index_map[val].append(idx)


        for qi in range(m):
            q = queries[qi]
            min_distance = float('inf')
            indices = index_map[nums[q]]
            pos = bisect.bisect_left(indices, q)
                
            left_j = indices[pos - 1]
            right_j = indices[(pos + 1) % len(indices)]
                
            for j in [left_j, right_j]:
                if j != q:
                    left_distance = abs(j - q)
                    right_distance = n - left_distance
                    min_distance = min(min_distance, left_distance, right_distance)
            result.append(min_distance if min_distance != float('inf') else -1)

        return result
